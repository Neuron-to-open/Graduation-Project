<template>
    <div v-if="showDialog">
        <div class="dialog-overlay" @click="closeDialog"></div>
        <div class="dialog-container">
            <h2>{{ dialogTitle }}</h2>
            <p>{{ dialogContent }}</p>
            <button @click="closeDialog">关闭</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Dialog',
    props: {
        dialogTitle: String,
        dialogContent: String,
        initialShow: Boolean
    },
    data() {
        return {
            showDialog: this.initialShow
        };
    },
    methods: {
        closeDialog() {
            this.showDialog = false;
        }
    },
    mounted() {
        // 如果初始状态要求打开对话框
        if (this.initialShow) {
            document.body.style.overflow = 'hidden'; // 防止滚动条出现
        }
    },
    beforeUnmount() {
        document.body.style.overflow = 'auto';
    }
};
</script>

<style scoped>
.dialog-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 999;
}

.dialog-container {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: #fff;
    padding: 20px;
    border-radius: 5px;
    z-index: 1000;
}
</style>