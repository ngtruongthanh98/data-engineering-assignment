<template>
  <div class="home-page">
    <header-component />

    <div class="home-page-body">
      <div class="row">
        <bar-chart
          class="bar-chart-1"
          :labels="labelArray"
          title="Table Size Bytes"
        />
        <pie-chart
          class="pie-chart-1"
          :labels="labelArray"
          :data="itemCountArray"
          title="Item count"
        />
      </div>

      <!-- <div class="row">
        <line-chart class="line-chart-1" />
      </div> -->
    </div>

    <copyright />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import Copyright from "@/components/Copyright";
import BarChart from "@/components/Chart/BarChart";
// import LineChart from "@/components/Chart/LineChart";
import PieChart from "@/components/Chart/PieChart";
import { getDescriseTable } from "@/services/analyse";

export default {
  name: "HomePage",
  data: function () {
    return {
      productData: {
        ItemCount: "",
        TableSizeBytes: "",
      },
      categoryData: {
        ItemCount: "",
        TableSizeBytes: "",
      },
      commentData: {
        ItemCount: "",
        TableSizeBytes: "",
      },
      labelArray: ["Product", "Category", "Comment"],
    };
  },
  components: {
    HeaderComponent,
    BarChart,
    // LineChart,
    PieChart,
    Copyright,
  },
  computed: {
    itemCountArray: function () {
      return [
        this.productData.ItemCount,
        this.categoryData.ItemCount,
        this.commentData.ItemCount,
      ];
    },
    // percent of each item count
    itemCountPercentArray: function () {
      let total =
        this.productData.ItemCount +
        this.categoryData.ItemCount +
        this.commentData.ItemCount;
      return [
        (this.productData.ItemCount / total) * 100,
        (this.categoryData.ItemCount / total) * 100,
        (this.commentData.ItemCount / total) * 100,
      ];
    },
    tableSizeBytesArray: function () {
      return [
        this.productData.TableSizeBytes,
        this.categoryData.TableSizeBytes,
        this.commentData.TableSizeBytes,
      ];
    },
  },
  methods: {
    async getDescriseTable(tableName) {
      try {
        const response = await getDescriseTable(tableName);

        console.log("response: ", response.data.Table.ItemCount);

        if (tableName === "Product") {
          this.productData.ItemCount = response.data.Table.ItemCount;
          this.productData.TableSizeBytes = response.data.Table.TableSizeBytes;
        } else if (tableName === "Category") {
          this.categoryData.ItemCount = response.data.Table.ItemCount;
          this.categoryData.TableSizeBytes = response.data.Table.TableSizeBytes;
        } else if (tableName === "Comment") {
          this.commentData.ItemCount = response.data.Table.ItemCount;
          this.commentData.TableSizeBytes = response.data.Table.TableSizeBytes;
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  mounted() {
    this.getDescriseTable("Product");
    this.getDescriseTable("Category");
    this.getDescriseTable("Comment");
  },
};
</script>

<style lang="scss" scoped>
.home-page {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;

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
