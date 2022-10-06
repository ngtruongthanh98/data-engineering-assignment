<template>
  <div class="product-detail">
    <div class="product-detail-body">
      <div class="title">Product Specifications</div>

      <div class="content">
        <div class="content-row">
          <div class="col-1">Category</div>
          <div class="col-2">Category > Sub Category > Product</div>
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
          <div class="col-1">Stock</div>
          <div class="col-2">1499</div>
        </div>
      </div>

      <div class="description">
        <div class="description-title">Product Description</div>
        <p>THÔNG TIN XUẤT BẢN:</p>
        <p>Tác giả: Shannon Thomas, LCSW</p>
        <p>Dịch giả: Trương Tuấn</p>
        <p>Giá bìa: 169,000đ</p>
        <p>Kích thước khổ:13x20,5</p>
        <p>Số trang: 328.</p>
        <p>Mã EAN: 8936066692298</p>
        <p>NXB liên kết:NXB Dân Trí</p>
        <p>
          Sách do Công ty TNHH Văn hóa và Truyền thông 1980 BOOKS ấn hành quý 1
          năm 2022
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style lang="scss">
.product-detail {
  padding: 24px;

  &-body {
    background-color: white;
    text-align: start;

    .title {
      padding: 24px;
      text-align: start;
    }

    .content {
      &-row {
        display: grid;
        grid-template-columns: 5fr 25fr;
        padding: 12px 24px;

        .col-1,
        .col-2 {
          text-align: left;
        }
      }
    }

    .description {
      padding: 24px;

      .description-title {
        padding-bottom: 24px;
      }
    }
  }
}
</style>