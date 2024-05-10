import chat from '@/pages/chat.vue'
import login from '@/pages/login.vue'
import register from '@/pages/register.vue'
import notfound from '@/pages/notfound.vue'
import visual from '@/pages/visual.vue'

import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {
            path: '/',
            name: 'register',
            component: register
        },
        {
            path: '/login',
            name: 'login',
            component: login
        },
        {
            path: '/chat',
            name: 'chat',
            component: chat
        },
        {
            path: '/visual',
            name: 'visual',
            component: visual
        },
        {
            path: '/:pathMatch(.*)*',
            name: 'notfound',
            component: notfound
        },
    ]
})

export default router
