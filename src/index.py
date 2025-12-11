from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_openai import ChatOpenAI

OPEN_AI_API_KEY = test

app = Flask(__name__)
# CORS 설정 - React 개발 서버(localhost:3000)에서의 요청 허용
CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:3000"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# POST /api/chat - 채팅 메시지 처리
@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        
        if not data or not data.get("message"):
            return jsonify({"error": "Message is required"}), 400
        
        user_message = data["message"]

        llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo', openai_api_key=OPEN_AI_API_KEY)
        response = llm.invoke(user_message)
        print(response.content)

        return jsonify({
            "response": response.content,
            "status": "success"
        }), 200
    except Exception as e:
        print(f"Chat endpoint error: {e}")
        return jsonify({
            "error": "서버 오류가 발생했습니다.",
            "status": "error"
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)

