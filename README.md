# Noor - Cedar Flow Automation business assistant
EECE 503P/798S, C3: Introduction to Agents.

## Run
1. `pip install -r requirements.txt`
2. `cp .env.example .env` and add your key (`LLM_PROVIDER=gemini` or `openai`)
3. Open `business_agent.ipynb`, or run `python app.py`

## Flow
message -> **router** (general / lead / feedback) -> intent-specific prompt + tools -> **agent loop** (tool calls) -> **reflection** (draft checked, revised) -> reply

Tool calls, router decisions and reflection drafts/revisions are printed and appended to `logs/events.jsonl`.

## Hugging Face Spaces (bonus)
Create a Gradio Space, upload `app.py`, `requirements.txt` and the `me/` folder, and add your API key (and `LLM_PROVIDER`) under Settings > Secrets.

`app.py` contains the same code as the notebook's app cells. `make_pdf.py` regenerates `me/about_business.pdf`.
