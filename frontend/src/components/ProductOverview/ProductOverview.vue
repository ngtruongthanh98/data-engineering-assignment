<template>
  <div class="product-overview">
    <div class="path">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">Homepage</el-breadcrumb-item>
        <el-breadcrumb-item>Category</el-breadcrumb-item>
        <el-breadcrumb-item>Sub Category</el-breadcrumb-item>
        <el-breadcrumb-item>Product</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

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

        <div class="information-box">
          <div class="row">
            <div class="col">Color</div>
            <div class="col">
              <div class="item-group">
                <item-tag
                  v-for="(color, index) in colorList"
                  :key="index"
                  :content="color"
                />
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col">Size</div>
            <div class="col">
              <div class="item-group">
                <item-tag
                  v-for="(size, index) in sizeList"
                  :key="index"
                  :content="size"
                />
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col">Style</div>
            <div class="col">Unknown</div>
          </div>

          <div class="row">
            <div class="col">Quantity</div>
            <div class="col">5000</div>
          </div>

          <div class="row">
            <div class="col">Sell Start Date</div>
            <div class="col">14/5/2014</div>
          </div>

          <div class="row">
            <div class="col">Sell Start End</div>
            <div class="col">None</div>
          </div>

          <div class="button-row">
            <el-button
              type="primary"
              class="direction-btn"
              @click="onClickTransactionDetail"
              >Transactions</el-button
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ItemTag from "@/components/ItemTag/ItemTag";

export default {
  data: function () {
    return {
      ratingValue: 4.9,
      colorList: ["Red", "Blue", "Yellow", "Green"],
      sizeList: ["XS", "S", "M", "L", "XL"],
    };
  },
  components: {
    ItemTag,
  },
  methods: {
    onClickTransactionDetail() {
      console.log("Clicked");

      const transaction = {
        id: 2424,
      };

      this.$router.push(`/transaction/${transaction.id}`);
    },
  },
};
</script>

<style lang="scss">
.product-overview {
  .path {
    text-align: start;
    margin-bottom: 24px;
  }

  padding: 24px 200px 0px 200px;

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
          color: #ee4d2d;
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

      .information-box {
        margin-top: 24px;
        .row {
          display: grid;
          grid-template-columns: 200px 5fr;
          align-items: center;
          width: 300px;
          padding: 12px 0;

          .col {
            text-align: start;

            .item-group {
              display: flex;
              gap: 10px;
            }
          }
        }

        .button-row {
          width: 100%;
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
  }
}
</style>