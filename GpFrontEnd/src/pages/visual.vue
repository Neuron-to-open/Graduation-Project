<template>
    <button @click="add">增加数据</button>
    <div ref="barChart" style="width: 600px; height: 400px;"></div>
</template>

<script lang="ts" setup name="visual">
    import { onMounted, ref } from 'vue';
    import * as echarts from 'echarts';
    import { REGISTRATION_API } from '@/utils/url';
    import qs from 'qs';
    import axios from 'axios';

    const barChart = ref(null);
    const llm = ref(null);
    const dataset = ref(null)
    const remark = ref(null)


    // async function getData() {
    //     const url = REGISTRATION_API + '/';
    //     const res = await fetch('https://www.fastmock.site/mock/a0d0d0a0f0e0d0c0b0a0b0c0d0e0f0g/api/getData');
    //     const data = await res.json();
    //     console.log(data);
    // }

    onMounted(() => {
        const chartInstance = echarts.init(barChart.value);
        const options = {
            title: {
            text: '基础柱状图'
            },
            tooltip: {},
            xAxis: {
            data: ['Shirt', 'Cardign', 'Chiffon Shirt', 'Pants', 'Heels', 'Socks']
            },
            yAxis: {},
            series: [{
            name: 'Sales',
            type: 'bar',
            data: [5, 20, 36, 10, 10, 20]
            }]
        };
        chartInstance.setOption(options);
    });


    async function add() {
        const url = REGISTRATION_API + '/add/';
        try {
            const response = await axios ( {
                method: 'post' ,
                url: url,
                data: qs.stringify({
                    llm: llm.value,
                    dataset: dataset.value,
                    remark: remark.value
                }) ,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }) ;

        } catch (error) {
            console.log(error)
        }
    }
</script>

<style scoped>
</style>