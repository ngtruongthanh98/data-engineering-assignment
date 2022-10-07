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
              <el-breadcrumb-item>Category</el-breadcrumb-item>
              <el-breadcrumb-item>Sub Category</el-breadcrumb-item>
              <el-breadcrumb-item>Product</el-breadcrumb-item>
            </el-breadcrumb>
          </div>
        </div>
        <div class="content-row">
          <div class="col-1">Brand</div>
          <div class="col-2">Unknown</div>
        </div>
        <div class="content-row">
          <div class="col-1">Language</div>
          <div class="col-2">English</div>
        </div>
        <div class="content-row">
          <div class="col-1">Plublishing Company</div>
          <div class="col-2">1980BOOKS</div>
        </div>
        <div class="content-row">
          <div class="col-1">Year</div>
          <div class="col-2">2020</div>
        </div>
        <div class="content-row">
          <div class="col-1">Stock</div>
          <div class="col-2">1499</div>
        </div>
        <div class="content-row">
          <div class="col-1">Weight</div>
          <div class="col-2">200 gram</div>
        </div>
      </div>

      <div class="documentation">
        <div class="documentation-title">Product Documentation</div>

        <div class="content">
          <div class="content-row">
            <div class="col-1">Title</div>
            <div class="col-2">Here is a title</div>
          </div>
          <div class="content-row">
            <div class="col-1">Document Level</div>
            <div class="col-2">High</div>
          </div>
          <div class="content-row">
            <div class="col-1">Owner</div>
            <div class="col-2">Mr. Brown</div>
          </div>
          <div class="content-row">
            <div class="col-1">Status</div>
            <div class="col-2">Completed</div>
          </div>
          <div class="content-row">
            <div class="col-1">Document Summary</div>
            <div class="col-2">Here is a summary for the document</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
.product-detail {
  padding: 24px 200px 0px 200px;

  &-body {
    background-color: white;
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

        border-top: 1px solid rgba(0, 0, 0, 0.09);
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