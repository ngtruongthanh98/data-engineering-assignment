<template>
  <div class="home-page">
    <header-component />

    <div class="home-page-body">
      <bar-chart class="bar-chart-1" />

      <line-chart class="line-chart-1" />
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import BarChart from "@/components/BarChart";
import LineChart from "@/components/LineChart";

export default {
  name: "HomePage",
  data: function () {
    return {};
  },
  components: {
    HeaderComponent,
    BarChart,
    LineChart,
  },
};
</script>

<style lang="scss" scoped>
.home-page {
  &-body {
    width: 100%;
    display: flex;
    justify-content: center;

    margin: 24px auto 24px auto;

    .bar-chart-1 {
      width: 400px;
      height: 400px;
      margin-right: 48px;
    }

    .line-chart-1 {
      width: 800px;
    }
  }
}
</style>
