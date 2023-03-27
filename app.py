import openai
import gradio


openai.api_key = "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"

messages = [{"role": "system", "content": "Tên: Cookie, Công việc: chatbot của Thái Tâm, email: tam.2174802010677@vanlanguni.vn, điện thoại: 0965225092, tên người phát triển: Lê Trần Thái Tâm,phản hồi dựa trên API từ chatGPT, bắt đầu trả lời luôn luôn giới thiệu các thông tin đã cung cấp"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply


gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Cookie ChatBot").launch(share=True)