<template>
  <div class="chat-container">
    <h1>paddlepaddle chatbot</h1>
    <h2 @click="tovisual">可视化</h2>
    <div class="messages">
      <div v-for="(message, index) in messages" :key="index" :class="`message ${message.sender}`">
        <div class="message-content">{{ message.text }}</div>
      </div>
    </div>
    <form @submit.prevent="sendMessage" class="message-form">
      <input v-model="userInput" placeholder="输入消息..." autofocus>
      <button type="submit">发送</button>
    </form>
  </div>
</template>


<script lang="ts" setup name="chat">

  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  import { REGISTRATION_API } from '@/utils/url';
  import axios from 'axios';
  import qs from 'qs'



  const messages:any = ref([])
  const userInput:any = ref('')

  const router = useRouter()


  async function getAnswer() {
    const url = REGISTRATION_API + '/chat/'
    try {
      const response = await axios ( {
          method: 'POST' ,
          url : url ,
          data : qs.stringify({
              message: userInput.value
          }) ,
          headers : {
              'Content-Type' : 'application/x-www-form-urlencoded' ,
          },
      } ) ;
      console.log(response.data)

      if (response.data.error_num == 0){
        const result = response.data      
        return result
      }
    } catch (error) {
      console.log(error)
    }

    return null
    // messages.value.push({ text: data.answer, sender: 'bot' })
  }

   /**
   * 发送消息功能，当用户输入消息后点击发送，将消息添加到聊天记录中，并模拟机器人回复。
   * 无参数
   * 无返回值
   */
  async function sendMessage() {
    if (userInput.value.trim()) {
      // 判断用户输入是否为空，不为空则添加到消息列表
      messages.value.push({ text: userInput.value, sender: 'user' })
      const result:any = await getAnswer()
      // 模拟延迟以仿真聊天机器人回答
      setTimeout(() => {
        console.log('result:', result['answer'])
        messages.value.push({ text: `这是你的消息: ${result['answer']}`, sender: 'bot' })
      }, 1000)
      // 发送后清空输入框
      userInput.value = ''
    }
  }

  /**
   * 跳转到可视化页面的功能。
   * 无参数
   * 无返回值
   */
  function tovisual() {
    router.push('/visual')
  }


</script>


<style scoped>
  .chat-container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    border-radius: 8px;
    display: flex;
    flex-direction: column;
    height: 90vh;
  }

  .messages {
    flex-grow: 1;
    overflow-y: auto;
    padding: 10px;
    display: flex;
    flex-direction: column;
  }

  .message {
    margin: 5px;
    padding: 10px;
    border-radius: 10px;
  }

  .message.user {
    align-self: end;
    background-color: #d1ecf1;
  }

  .message.bot {
    align-self: start;
    background-color: #f8d7da;
  }

  .message-content {
    max-width: 80%;
  }

  .message-form {
    display: flex;
    margin-top: 10px;
  }

  input {
    flex-grow: 1;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 8px;
  }

  button {
    padding: 10px 20px;
    border: none;
    background-color: #007bff;
    color: white;
    cursor: pointer;
    border-radius: 8px;
  }

  #chat {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
</style>