from youtube_transcript_api import YouTubeTranscriptApi
from datetime import timedelta
import argparse
import re

def get_video_id(url):
    """Extract the video ID from the YouTube URL."""
    video_id_match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return video_id_match.group(1) if video_id_match else None

def save_transcript(transcript, output_file):
    """Save the transcript to a text file."""
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(transcript)
    except Exception as e:
        print(f"Error: {e}")

def fetch_transcript_with_api(video_id, text_only):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        if text_only:
            return " ".join([line['text'] for line in transcript])
        else:
            return "\n".join([f"{str(timedelta(seconds=round(line['start'])))}: {line['text']}" for line in transcript])
    except Exception as e:
        print(f"Error: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="Fetch a YouTube video's transcript via the API "
                                    + "and save it to a file for notes or to summarize with an LLM "
                                    + "agent.")
    parser.add_argument('-u', '--url',
                        help="The URL of the video including the video ID. May not work if other "
                            + "referrals/data is in the URL.")
    parser.add_argument('-o', '--output',
                        help="The name of the file in which to save the transcript. Default: "
                        + "transcript.txt", default="transcript.txt")
    parser.add_argument('-t', '--text-only',
                        help="Omits the timestamp from the transcript file and concatenates the transcript "
                        + "into a single line.",
                        action='store_true')
    
    args = parser.parse_args()

    if args.url is None:
        print("[!] URL is required. Example: python3 fetch-transcript.py "
              + "-u https://www.youtube.com/watch?v=dQw4w9WgXcQ "
              + "[-o output_file.txt] [--text-only]")
        sys.exit(1)

    video_id = get_video_id(args.url)

    if not video_id:
        print("[!] Invalid YouTube URL.")
        sys.exit(1)

    print("[*] Fetching transcript...")
    transcript = fetch_transcript_with_api(video_id, args.text_only)

    if transcript:
        print("[*] Transcript fetched successfully.")
        save_transcript(transcript, args.output)
        print(f"[*] Transcript saved to {args.output}")
    else:
        print("No transcript found or an error occurred.")

if __name__ == "__main__":
    main()