# Transcript Fetcher

Uses the YouTube API to grab the transcript for a target video and outputs it to a local file.

You can get the output with timestamps (default) or without timestamps, then upload the transcript to your desired LLM for summarization. I have included a basic prompt that worked pretty well with ChatGPT to include in my Obsidian repository.

I also included a small JavaScript snippet that you could put in your browser instead, but why do that...

Written mostly by ChatGPT - it's come a long way. I just made it a little nicer and added better argument parsing, but the code worked out of the gate.

# Usage

## Install
It only requires Python and the YouTube transcript API (consists of a few things). As always, a virtual environment is recommended.

```
git clone https://github.com/BCHarrell/fetch-transcript.git
cd fetch-transcript
pip3 install -r requirements.txt
```

## Example usage:

With timestamps:
```
python3 .\fetch-transcript.py -u 'https://www.youtube.com/live/-yf-e-9FvOc' -o Berkeley_Lecture7.txt
# [*] Fetching transcript...
# [*] Transcript fetched successfully.
# [*] Transcript saved to Berkeley_Lecture7.txt

# head Berkeley_Lecture7.txt
# 0:00:00: NICOLAS CHAPADOS: We're both 
# very thrilled to be here.
# 0:00:02: Super happy.
# 0:00:03: Thanks for the invitation.
# 0:00:04: Again, it's already
```

Without timestamps:
```
python3 .\fetch-transcript.py -u 'https://www.youtube.com/live/-yf-e-9FvOc' -o Berkeley_Lecture7.txt --text-only
# [*] Fetching transcript...
# [*] Transcript fetched successfully.
# [*] Transcript saved to Berkeley_Lecture7.txt

# cat Berkeley_Lecture7.txt
# NICOLAS CHAPADOS: We're both very thrilled to be here. Super happy. Thanks for the invitation. Again, it's already the midpoint...
```

### ChatGPT Prompt:
```
Please summarize the attached document consisting of a YouTube video transcript and timestamps in the format hh:mm:ss. Supply the summary in Markdown that can be copied into Obsidian (in other words, put it in a code block with the appropriate syntax) and include the following sections. I have included a description of what each section should include in {}

# Overview:
{A 2-3 sentence overview of the summarized material}

## Key points:
{2-3 bullets of the most important points}

# Main Content
{A full summary of the material. Do not include any information not found in the transcript}

For the full summary, put timestamps indicating where the information came from. The timestamps do not need to indicate each line of the transcript. For example:

(14:30) Clear instructions are important for LLMs. To get clarity, Brent discussed the following tips...
(15:34) Brent then discussed...

Do not consolidate more than 5 minutes of material into each portion of the summary. In other words, provide more details than a default summary.
```

Output:
```
# Overview:
The lecture by Nicolas Chapados and Alexandre Drouin from ServiceNow Research discusses advancements in AI agents for enterprise workflows. It introduces new frameworks like TapeAgents and BrowserGym, focusing on building, optimizing, and evaluating LLM-powered API and web agents. The session explores practical examples, challenges, and benchmarks for developing robust AI agents that can assist with real-world tasks in enterprise settings.

## Key Points:
- The integration of LLMs with API and web agents can help automate complex, manual enterprise tasks.
- New frameworks like TapeAgents and BrowserGym provide structured tools for developing, debugging, and optimizing AI agents.
- Despite promising capabilities, AI agents still face challenges in robustness, efficiency, and handling complex workflows reliably.

# Main Content

(00:00:00) **Introduction**  
Nicolas Chapados starts the lecture by framing the discussion around AI agents used in enterprise workflows. He introduces ServiceNow, a platform specializing in automating workflows across various domains like IT, HR, and customer support. The goal is to explore how AI agents can enhance user productivity by automating repetitive and complex tasks.

...
```