<template>
  <div class="transaction-page">
    <header-component />
    <h1>Transaction Table</h1>

    <div class="transaction-page-body">
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column
          prop="transactionId"
          label="Transaction ID"
          width="180"
        >
        </el-table-column>
        <el-table-column prop="productId" label="Product ID" width="100">
        </el-table-column>
        <el-table-column
          prop="transactionDate"
          label="Transaction Date"
          width="180"
        >
        </el-table-column>
        <el-table-column prop="transactionType" label="Transaction Type">
        </el-table-column>
        <el-table-column prop="quantity" label="Quantity"> </el-table-column>
        <el-table-column prop="actualCost" label="Actual Cost">
        </el-table-column>
      </el-table>

      <div class="button-row">
        <el-button
          type="primary"
          class="direction-btn"
          @click="onClickProductDetail"
          >Product Details</el-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";

export default {
  name: "TransactionPage",
  data: function () {
    return {
      tableData: [
        {
          transactionId: "100093",
          productId: "784",
          transactionDate: "2007-09-01 00:00:00.000",
          transactionType: "W",
          quantity: "42424",
          actualCost: "1716.5304",
        },
        {
          transactionId: "100094",
          productId: "7846",
          transactionDate: "2007-09-01 00:00:00.000",
          transactionType: "W",
          quantity: "7575",
          actualCost: "1716.5304",
        },
        {
          transactionId: "100095",
          productId: "5325",
          transactionDate: "2007-09-01 00:00:00.000",
          transactionType: "S",
          quantity: "7578",
          actualCost: "1716.5304",
        },
        {
          transactionId: "100096",
          productId: "5747",
          transactionDate: "2007-09-01 00:00:00.000",
          transactionType: "S",
          quantity: "36385",
          actualCost: "1716.5304",
        },
      ],
    };
  },
  components: {
    HeaderComponent,
  },
  methods: {
    onClickProductDetail() {
      console.log("Clicked");

      const product = {
        id: 2424,
      };

      this.$router.push(`/product/${product.id}`);
    },
  },
};
</script>

<style lang="scss" scoped>
.transaction-page {
  &-body {
    margin: 24px 200px 24px 200px;

    .button-row {
      text-align: right;
    }
    .direction-btn {
      margin-top: 24px;
      background-color: #ee4d2d;
      border-color: #ee4d2d;

      &:hover {
        background-color: #ff5a3d;
      }
    }
  }
}
</style>
