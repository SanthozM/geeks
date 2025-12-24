# Running Gemma 3 Locally on Intel N100 (8GB RAM)
## Complete Installation Guide: Ollama + Open WebUI and Low-Memory AirLLM-Style Setup

---

## What You Will Build

With this you can set up **two local AI stacks**, Choose the one fits for you:

1. **Ollama + Open WebUI**
2. **Low-memory AirLLM-style CPU setup**

---

## System Requirements

- OS: Ubuntu 22.04 / Debian 12
- CPU: Intel N100
- RAM: 8GB
- Storage: 20GB free
- GPU: Not required

---
# **Ollama + Open WebUI**
## 1. Base System Preparation

```bash
sudo apt update && sudo apt -y upgrade
sudo apt -y install curl git python3 python3-venv python3-pip htop
```

---

## 2. Install Docker

```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker $USER
newgrp docker
docker --version
```

---

## 3. Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
sudo systemctl enable --now ollama
ollama --version
```

---

## 4. Download Gemma 3

```bash
ollama pull gemma3:1b
# or
ollama pull gemma3:4b
```

Test:
```bash
ollama run gemma3:1b
```

---

## 5. Install Open WebUI

```bash
docker run -d \
  -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Open:
```bash
xdg-open http://localhost:3000
```

---

# **Low-memory AirLLM-style CPU setup**

## 1. Create virtual environment

```bash
mkdir -p ~/gemma_air_ui
cd ~/gemma_air_ui
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -U pip wheel
pip install -U transformers accelerate safetensors sentencepiece gradio
```

---

## 2. Hugging Face Login

```bash
pip install -U huggingface_hub
huggingface-cli login
```

---

## 3. Create Chatbot UI

Create `app.py` and paste the code the below code.

```python
import os
import gradio as gr
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = os.environ.get("MODEL_ID", "google/gemma-3-4b-it")
OFFLOAD_DIR = os.environ.get("OFFLOAD_DIR", "./offload")

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    offload_folder=OFFLOAD_DIR,
    torch_dtype=torch.float32,
    low_cpu_mem_usage=True,
)

def chat(user_msg, history):
    if history is None:
        history = []

    prompt = ""
    for u, a in history:
        prompt += f"User: {u}\nAssistant: {a}\n"
    prompt += f"User: {user_msg}\nAssistant:"

    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )

    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    answer = text.split("Assistant:", 1)[-1].strip()
    history.append((user_msg, answer))
    return history, history

with gr.Blocks(title="Gemma 3 CPU Chat") as demo:
    gr.Markdown("## Gemma 3 Chatbot (CPU + Disk Offload)")
    chatbot = gr.Chatbot(height=420)
    msg = gr.Textbox(label="Type your message")
    state = gr.State([])
    send = gr.Button("Send")

    send.click(chat, [msg, state], [chatbot, state])
    msg.submit(chat, [msg, state], [chatbot, state])

demo.launch(server_name="0.0.0.0", server_port=7860)

```

---

## 4. Run Chatbot

```bash
export MODEL_ID="google/gemma-3-4b-it"
export OFFLOAD_DIR="$HOME/gemma_air_ui/offload"
mkdir -p "$OFFLOAD_DIR"
python app.py
```

Open:
```bash
xdg-open http://localhost:7860
```

---

## Conclusion

You now have **Gemma 3 running locally** on Intel N100 using:
- Ollama + Open WebUI
- Low-memory CPU chatbot UI
