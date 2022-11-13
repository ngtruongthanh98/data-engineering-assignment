<template>
  <div class="product-detail">
    <div class="product-detail-body">
      <div class="title">Product Specifications</div>

      <div class="content">
        <div class="content-row">
          <div class="col-1">Category</div>
          <div class="col-2">
            <el-breadcrumb separator-class="el-icon-arrow-right">
              <!-- <el-breadcrumb-item :to="{ path: '/' }">Homepage</el-breadcrumb-item> -->
              <el-breadcrumb-item>{{ categoryName }}</el-breadcrumb-item>
              <el-breadcrumb-item>{{ subCategoryName }}</el-breadcrumb-item>
              <el-breadcrumb-item>{{ productName }}</el-breadcrumb-item>
            </el-breadcrumb>
          </div>
        </div>
        <div class="content-row">
          <div class="col-1">Brand</div>
          <div class="col-2">{{ brand }}</div>
        </div>
        <div class="content-row">
          <div class="col-1">Language</div>
          <div class="col-2">{{ language }}</div>
        </div>
        <div class="content-row">
          <div class="col-1">Culture</div>
          <div class="col-2">{{ culture }}</div>
        </div>
        <div class="content-row">
          <div class="col-1">Plublishing Company</div>
          <div class="col-2">{{ producer }}</div>
        </div>
        <div class="content-row">
          <div class="col-1">Year</div>
          <div class="col-2">{{ sellStartDate }}</div>
        </div>
        <div class="content-row">
          <div class="col-1">Stock</div>
          <div class="col-2">{{ quantity }}</div>
        </div>
        <div class="content-row">
          <div class="col-1">Weight</div>
          <div class="col-2">{{ weight }} gram</div>
        </div>
      </div>

      <div class="documentation">
        <div class="documentation-title">Product Documentation</div>

        <div class="content">
          <div class="content-row">
            <div class="col-1">Title</div>
            <div class="col-2">{{ title }}</div>
          </div>
          <div class="content-row">
            <div class="col-1">Document Level</div>
            <div class="col-2">{{ documentLevel }}</div>
          </div>
          <div class="content-row">
            <div class="col-1">Owner</div>
            <div class="col-2">{{ owner }}</div>
          </div>
          <div class="content-row">
            <div class="col-1">Status</div>
            <div class="col-2">{{ status }}</div>
          </div>
          <div class="content-row">
            <div class="col-1">Document Summary</div>
            <div class="col-2">{{ documnentSummary }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    productName: {
      type: String,
      default: "HL Nipple",
    },
    categoryName: {
      type: String,
      default: "Category",
    },
    subCategoryName: {
      type: String,
      default: "Sub Category",
    },
    brand: {
      type: String,
      default: "Unknown",
    },
    language: {
      type: String,
      default: "English",
    },
    culture: {
      type: String,
      default: "English",
    },
    producer: {
      type: String,
      default: "Unknown",
    },
    sellStartDate: {
      type: String,
      default: "2020-01-01",
    },
    sellEndDate: {
      type: String,
      default: "Unknown",
    },
    quantity: {
      type: Number || String,
      default: 1499,
    },
    weight: {
      type: Number,
      default: 200,
    },
    title: {
      type: String,
      default: "Here is a title",
    },
    documentLevel: {
      type: String,
      default: "High",
    },
    owner: {
      type: String,
      default: "Mr. Brown",
    },
    status: {
      type: String,
      default: "Completed",
    },
    documnentSummary: {
      type: String,
      default: "Here is a summary for the document",
    },
  },
};
</script>

<style lang="scss">
.product-detail {
  padding: 24px 200px 0px 200px;

  &-body {
    background-color: $color-white;
    text-align: start;
    padding-bottom: 12px;

    .title {
      font-size: 18px;
      padding: 24px;
      text-align: start;
    }

    .content {
      &-row {
        display: grid;
        grid-template-columns: 10fr 25fr;
        padding: 12px 24px;

        .el-breadcrumb__item {
          font-size: 16px;
        }

        .col-1,
        .col-2 {
          text-align: left;
        }
      }
    }

    .documentation {
      padding-top: 24px;

      .documentation-title {
        font-size: 18px;
        margin-left: 24px;
        margin-right: 24px;
        padding-top: 24px;
        padding-bottom: 24px;

        border-top: 1px solid $color-border-tag;
      }

      .content {
        &-row {
          display: grid;
          grid-template-columns: 10fr 25fr;
          padding: 12px 24px;

          .el-breadcrumb__item {
            font-size: 16px;
          }

          .col-1,
          .col-2 {
            text-align: left;
          }
        }
      }
    }
  }
}
</style>