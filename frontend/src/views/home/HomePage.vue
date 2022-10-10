<template>
  <div class="home-page">
    <header-component />

    <div class="home-page-body">
      <div class="row">
        <bar-chart class="bar-chart-1" />
        <pie-chart class="pie-chart-1" />
      </div>

      <div class="row">
        <line-chart class="line-chart-1" />
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import BarChart from "@/components/Chart/BarChart";
import LineChart from "@/components/Chart/LineChart";
import PieChart from "@/components/Chart/PieChart";

export default {
  name: "HomePage",
  data: function () {
    return {};
  },
  components: {
    HeaderComponent,
    BarChart,
    LineChart,
    PieChart,
  },
};
</script>

<style lang="scss" scoped>
.home-page {
  &-body {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;

    margin: 24px auto 24px auto;

    .row {
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .bar-chart-1 {
      width: 400px;
      height: 400px;
      margin-right: 48px;
    }

    .line-chart-1 {
      width: 800px;
      height: 300px;
    }

    .pie-chart-1 {
      margin-top: 24px;
    }
  }
}
</style>
