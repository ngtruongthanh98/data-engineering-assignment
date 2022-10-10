<template>
  <div class="home-page">
    <header-component />

    <div class="home-page-body">
      <bar-chart class="bar-chart-1" />
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import BarChart from "@/components/BarChart";

export default {
  name: "HomePage",
  data: function () {
    return {};
  },
  components: {
    HeaderComponent,
    BarChart,
  },
};
</script>

<style lang="scss" scoped>
.home-page {
  &-body {
    .bar-chart-1 {
      width: 300px;
      height: 300px;
    }
  }
}
</style>
