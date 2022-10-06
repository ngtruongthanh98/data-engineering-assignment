<template>
  <div class="product-overview">
    <div class="path">Category > Sub Category > Product</div>

    <div class="product-overview-body">
      <div class="image-box">
        <img
          src="https://media.wiley.com/product_data/coverImage300/82/15095467/1509546782.jpg"
          alt="book"
        />
      </div>

      <div class="product-overview-body-content">
        <div class="product-name">
          <div class="title">
            <span class="category">Category</span>
            <span> - </span>
            <span class="content">Book Wars</span>
            <span> - </span>
            <span>Nha san xuat</span>
          </div>
        </div>
        <div class="product-id">
          <div class="title">
            Product ID: <span class="content">BOOKGG67GD74H</span>
          </div>
        </div>
        <div class="rating-box">
          <div class="rating">
            <div class="title">4.9</div>
            <el-rate v-model="ratingValue" :max="5"></el-rate>
          </div>
        </div>

        <div class="price-box">
          <div class="price">
            <div class="title">
              <span class="content">$49.99</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data: function () {
    return {
      ratingValue: 4.9,
    };
  },
};
</script>

<style lang="scss">
.product-overview {
  .path {
    text-align: start;
    margin-bottom: 24px;
  }

  padding: 24px;

  &-body {
    display: flex;
    justify-content: center;
    width: 100%;

    background-color: white;

    .image-box {
      padding: 24px;
    }

    &-content {
      display: flex;
      flex-direction: column;
      align-items: start;
      padding: 24px;

      .product-name {
        font-size: 24px;
        font-weight: 700;
      }

      .product-id {
      }

      .rating-box {
        .rating {
          color: red;
          display: flex;
          align-items: center;

          .title {
            margin-right: 5px;
          }
        }
      }

      .price-box {
        margin-top: 16px;

        .price {
          font-size: 24px;
        }
      }
    }
  }
}
</style>