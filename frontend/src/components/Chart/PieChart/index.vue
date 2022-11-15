<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="chart-component">
    <Pie
      :chart-options="chartOptions"
      :chart-data="chartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
      :title="title"
    />

    <div class="chart-name">{{ title }}</div>
  </div>
</template>

<script>
import { Pie } from "vue-chartjs/legacy";

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from "chart.js";

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);

export default {
  name: "PieChart",
  components: {
    Pie,
  },
  props: {
    chartId: {
      type: String,
      default: "pie-chart",
    },
    datasetIdKey: {
      type: String,
      default: "label",
    },
    width: {
      type: Number,
      default: 400,
    },
    height: {
      type: Number,
      default: 400,
    },
    cssClasses: {
      default: "",
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Array,
      default: () => [],
    },
    labels: {
      type: Array,
      default: () => [],
    },
    data: {
      type: Array,
      default: () => [],
    },
    title: {
      type: String,
      default: "",
    },
  },
  data() {
    return {
      chartData: {
        // labels: ["VueJs", "EmberJs", "ReactJs", "AngularJs"],
        labels: this.labels,
        datasets: [
          {
            backgroundColor: ["#41B883", "#E46651", "#00D8FF", "#DD1B16"],
            // data: [40, 20, 80, 10],

            // data: [189166902, 12218562, 146171],
            data: [31217, 317, 21002],
          },
        ],
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
      },
    };
  },
  computed: {
    itemCountPercentArray: function () {
      // total value of elements in data array
      const total = this.data.reduce((a, b) => a + b, 0);
      // find percent in total of each item in data array
      return this.data.map((item) => (item / total) * 100);
    },
  },
};
</script>

<style lang="scss">
.chart-component {
  .chart-name {
    font-size: 1.5rem;
    font-weight: 600;
    margin-top: 1rem;
  }
}
</style>
