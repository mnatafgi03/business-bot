# Noor: Business Assistant Agent for Cedar Flow Automation

My submission for the C3 assignment (Introduction to Agents) in EECE 503P/798S: Agentic Systems at AUB.

I built a chatbot agent for a fictional company I made up, **Cedar Flow Automation**, a small consultancy in Beirut that helps businesses with workflow automation, Odoo ERP setups and AI agents. The agent is called **Noor** and acts as the company's virtual concierge.

## What it does
- Answers questions about the business using a PDF profile and a short text summary
- Routes every message to the right handling path: general question, lead collection, or feedback
- Collects leads (name, email, notes) through a tool call
- Logs feedback and questions it can't answer through a second tool call
- Runs as a chatbot in Gradio, using the Gemini API
- Bonus: a reflection step where the agent checks its own draft before replying

## Project files
- `business_agent.ipynb`: the main notebook (I ran it on Google Colab)
- `app.py`: the same code as a plain Python script
- `me/about_business.pdf`: the business profile
- `me/business_summary.txt`: short summary of the business
- `requirements.txt`: libraries used
- `make_pdf.py`: script that generated the PDF

## How it works
1. **Persona vs. instructions:** I kept them separate in the notebook. The persona defines who Noor is and her tone. The instructions are the rules she follows, like never inventing prices and always asking for an email before ending a lead conversation.
2. **Router:** each message is first classified by a short LLM call into `general_question`, `lead_collection` or `feedback`. It also sees the last few messages, so a reply with just an email still counts as a lead. If the call fails (for example because of rate limits), simple keyword rules take over. Each intent gets its own task prompt and its own allowed tool.
3. **Tools:**
   - `record_customer_interest(email, name, message)` saves a lead and rejects invalid emails
   - `record_feedback(question)` logs feedback or a question Noor couldn't answer
   - Both print their output and write to `logs/events.jsonl`. Their schemas (name, description, input and output) are documented in the notebook.
4. **Agent loop:** the system prompt, chat history and allowed tools go to the model. If it calls a tool, the code runs it and gives the result back. Otherwise the text reply is returned.
5. **Reflection (bonus):** before replying, the model reviews its draft against the instructions and business info, then revises it if needed. Both versions are logged.
6. **Gradio:** a `ChatInterface` wraps the whole thing.

## How to run it
**On Colab (what I did):**
1. Upload `business_agent.ipynb` and the `me/` folder
2. Add `GEMINI_API_KEY` under Secrets (the key icon) and turn on notebook access
3. Run the notebook from the top

**Locally:**
1. `pip install -r requirements.txt`
2. Create a `.env` file with `LLM_PROVIDER=gemini` and `GEMINI_API_KEY=your-key`
3. Run `python app.py`

My API key is not in this repo.

## Notes
- The Gemini free tier allows only about 5 requests per minute per model. Each message makes around 3 calls (router, answer, reflection), so I paused between messages while testing. The code retries when it hits the limit, and setting `ENABLE_REFLECTION=false` reduces the number of calls.
- I didn't do the Hugging Face deployment bonus.
