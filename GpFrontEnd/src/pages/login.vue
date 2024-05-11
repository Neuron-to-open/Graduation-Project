<!--
  This example requires some changes to your config:
  
  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
      // ...
      require('@tailwindcss/forms'),
    ],
  }
  ```
-->
<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-white">
    <body class="h-full">
    ```
  -->
  <div class="flex min-h-full flex-1 flex-col justify-center px-6 py-12 lg:px-8">
    <div class="sm:mx-auto sm:w-full sm:max-w-sm">
      <img class="mx-auto h-200 w-auto" src="@/assets/girl.png"/>
      <h2 class="mt-10 text-center text-2xl font-bold leading-9 tracking-tight text-gray-900">登录你的账户</h2>
    </div>

    <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
      <div class="space-y-6">
        <div>
          <label for="name" class="block text-sm font-medium leading-6 text-gray-900">名称</label>
          <div class="mt-2">
            <input id="name" name="name" type="name"  class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" v-model="username"
          </div>
        </div>

        <div>
          <div class="flex items-center justify-between">
            <label for="password" class="block text-sm font-medium leading-6 text-gray-900">密码</label>
            <div class="text-sm">
              <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
            </div>
          </div>
          <div class="mt-2">
            <input id="password" name="password" type="password" class="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" v-model="password"/>
          </div>
        </div>

        <div>
          <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
          @click="login">
          Sign in</button>
        </div>
      </div>
    </div>
  </div>
</template>



<script lang="ts" setup name="login">


  import { ref } from 'vue'
  import { useRouter } from 'vue-router';
  import axios from 'axios'
  import qs from 'qs'
  import { REGISTRATION_API } from '@/utils/url';


  const username = ref('')
  const password = ref('')


  const router = useRouter()
  function tochat() {
    router.push('/chat')
  }


  // 可以定义一个通用的错误处理函数，以统一处理错误
  function handleError(error:any) {
    console.error("Error sending POST request:", error);
    // 此处可以调用UI组件方法，来显示错误信息给用户
    alert(error.message)
  }

  async function login() {
    // const config = {
    //   headers: {
    //     'Content-Type': 'application/x-www-form-urlencoded'
    //   }
    // }
    const url = REGISTRATION_API + "/login/"
    try {
      const internalResponse = await axios( {
        method: 'post',
        url: url,
        data: qs.stringify({
          username: username.value,
          password: password.value
        }) ,
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      });
      console.log(internalResponse.data)

      if (internalResponse.data.error_num == 0) {
        alert("登录成功")
        tochat()
      } else {
        alert("登陆失败")
      }
    } catch (error) {
      handleError(error);
    }
      
  }



</script>

<style scoped>
  .bakckground {
    background: url('../assets/girl.png') no-repeat center center fixed;
    background-size: cover;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
