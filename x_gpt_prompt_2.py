import os
import openai

# Safely read your API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set! "
                        "Please set it before running this script.")


def summarize_and_create_threads():
    # 1. Read your Driveline podcast transcript from dlpod.txt
    with open("/driveline_tools/podcast_content/dlpod.txt", "r", encoding="utf-8") as file:
        transcript_text = file.read()

    
    # 2. Craft the prompt for ChatGPT:
    #    - Provide the instructions about creating engaging social media content.
    #    - Insert the entire transcript as context.
    prompt = f"""
You are an expert at creating engaging social media content designed for X. 
You are also familiar with Driveline Baseball's philosophies and their blogs 
at https://www.drivelinebaseball.com/blog/.

Create 10 pieces of "threads" content for X that are detailed and specific 
to ideas and concepts that are discussed in the most recent Driveline Baseball 
podcast. The transcription of that podcast is provided below. 

Below is the transcribed content from the file 'dlpod.txt':
\"\"\"{transcript_text}\"\"\"

Disclaimer: Below is an example thread. Make sure to include a hook at the beginning 
of the threads and a call to action at the end of the threads. Each thread should be somewhat similar in character amount to the example thread below. 
Each thread should live between 4-10 segments.

[1. If you’re trying to get more mobile, the first step is to train at a high intent, expressing force in exercises that allow for as much ROM as possible. But you also need some type of passive work to really unlock the ability to relax into deep ranges. Here’s the science⬇️ 

2. First you need to understand exactly how your nervous system knows where your muscles are in space. There’s two main sensory units at play here- Golgi tendon organs and Muscle spindles 

3. Muscle Spindles detect both the amount of change in muscle length and the rate of that change. Think of their function like the seatbelt mechanism in a car. Lengthen the belt too fast or too far, and it triggers a contraction. 

4. This is called the stretch reflex, and it is monosynaptic- meaning that it from the spindle, to motor neurons in the spinal cord, and right to the muscle. Instantaneously. 

5. Golgi tendon organs detect mechanical tension between the muscle, tendon,and bone. Think of the GTO as functioning like a crane scale. 

6. When tension becomes too high, the GTOs trigger an inverse stretch reflex, causing the muscle to relax to prevent damage. This reflex is polysynaptic- meaning it takes a bit longer than the stretch reflex 

7. The non sensory pieces of the muscle itself can be segmented into two halves: Contractile and Non-Contractile Contractile elements produce force through actin-myosin cross bridging, Non-contractile run alongside the contractile elements and provide stability and support

8. Why deep ranges of passive stretching allow you to access ranges that active work doesn’t, is they don’t activate the muscle spindles stretch reflex as much, and allow the force to go onto the non-contractile elements. 

9. The formula here is just enough force to put you in deep positions, but not too much force too quickly that will make the muscle spindles activate contractile elements via the stretch reflex and nerf your ROM 

10. The main thing to consider here is this is a neurological adaptation- one that will be very important to high level throwing. There’s a certain amount of relaxation needed to achieve the ranges needed in a elite throw 

11. Obviously, the most important thing is to be able to produce force through these ranges, and you need the contractile elements to be able to do that. But passive work is valuable too, and is undeniably Lindy 

12. I think the most important takeaway here is that muscles aren’t just dumb pieces of meat. They’re highly tuned sensory units, and the reason why the best athletes in the world are they way they are is because of the software, not just the hardware. Happy Hunting. 
]

Take as long as needed to make content that is realistic and strictly based on the concepts that are talked about in the podcast.
"""

    # 3) Use the new 1.0.0+ global client interface for chat completions
    response = openai.chat.completions.create(
        model="gpt-4o",  # Ensure you have gpt-4 access on your account
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7, #alter for creativity
        max_tokens=10000 #8000-32000 is optimal in 4o (apparently)
    )
    
    # 4) Extract the model's response
    chatgpt_answer = response.choices[0].message.content
    
    # 5. Print or save the response
    print(chatgpt_answer)

if __name__ == "__main__":
    summarize_and_create_threads()