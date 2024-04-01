<template>
    <div class="chat-box">
        <div class="message-list">
            <div v-for="(message, index) in messages" :key="index" class="message"
                :class="{ 'self': message.sender === 'me', 'other': message.sender !== 'me' }">
                <span>{{ message.content }}</span>
            </div>
        </div>

        <form @submit.prevent="sendMessage">
            <input ref="inputMessage" type="text" placeholder="请输入消息..." v-model="newMessage"
                @keydown.enter="sendMessage" />
            <button type="submit">发送</button>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            messages: [
                // 初始消息数据，你可以从服务器获取或者初始化一些示例消息
                { sender: 'other', content: '你好，世界！' },
                { sender: 'me', content: '你好！' }
            ],
            newMessage: ''
        };
    },
    methods: {
        sendMessage() {
            if (this.newMessage.trim()) {
                this.messages.push({ sender: 'me', content: this.newMessage });
                this.newMessage = '';
                // 在此处模拟发送消息到服务器，实际项目中应调用API接口
            }
        }
    }
};
</script>

<style scoped>
.chat-box {
    position: relative;
    height: 400px;
    overflow-y: scroll;
}

.message {
    margin-bottom: 10px;
    padding: 10px;
    border-radius: 5px;
    max-width: 80%;

    &.self {
        text-align: right;
        background-color: #e0f7fa;
    }

    &.other {
        text-align: left;
        background-color: #b2dfdb;
    }
}

form {
    position: absolute;
    bottom: 0;
    width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    box-sizing: border-box;
}

input {
    flex-grow: 1;
    margin-right: 10px;
    padding: 5px;
    border: none;
    border-radius: 5px;
}

button {
    padding: 5px 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
</style>