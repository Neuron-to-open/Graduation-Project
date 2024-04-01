import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import Test from '../views/Test.vue' 
import ChatBox from '../views/ChatBox.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/test',
      name: 'test',
      component: Test
    },
    {
      path: '/ChatBox',
      name: 'ChatBox',
      component: ChatBox
    }
  ]
})

export default router
