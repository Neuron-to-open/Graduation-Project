<script setup>
  import { ref } from 'vue';
  

  const responseData = ref('');
  
  const sendData = async () => {
    // 示例数据
    const dataToSend = {
      message: "Hello from Vue 3!",
    };
  
    try {
      // 替换成你的后端接口URL
      const response = await fetch('http://localhost:8000/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(dataToSend),
      });
      const data = await response.json();
      responseData.value = data;
      alert("数据发送成功!");
    } catch (error) {
      console.error('发送数据时出错:', error);
      alert("发送数据成功");
    }
  };
  </script>
  

  <template>
    <div id="app">
      <button @click="sendData">发送数据</button>
    </div>
  </template>