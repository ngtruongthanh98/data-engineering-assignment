<template>
  <div class="transaction-page">
    <header-component />
    <div class="title">Transaction Table</div>

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
    <copyright />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import Copyright from "@/components/Copyright";

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
    Copyright,
  },
  methods: {
    onClickProductDetail() {
      const product = {
        productName: "Books",
      };

      this.$router.push(`/product/${product.productName}`);
    },
  },
};
</script>

<style lang="scss" scoped>
.transaction-page {
  .title {
    padding: 24px;
    font-size: 24px;
  }

  &-body {
    margin: 24px 200px 24px 200px;

    .button-row {
      text-align: right;
    }
    .direction-btn {
      margin-top: 24px;
      background-color: $color-primary;
      border-color: $color-primary;

      &:hover {
        background-color: $color-secondary;
      }
    }
  }
}
</style>
