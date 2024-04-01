<template>
    <div>
        <!-- 其他内容 -->
        <button @click="openDialog">打开对话框</button>
        <Dialog :dialog-title="'提示信息'" :dialog-content="'Hello World!'" :initial-show="isDialogOpen" />
    </div>
</template>

<script>
import Dialog from '@/components/Dialog.vue';

export default {
    components: {
        Dialog
    },
    data() {
        return {
            isDialogOpen: false
        };
    },
    methods: {
        openDialog() {
            this.isDialogOpen = true;
        }
    }
};
</script>