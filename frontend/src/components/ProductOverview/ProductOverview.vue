<template>
  <div class="product-overview">
    <div class="path">
      <el-breadcrumb separator-class="el-icon-arrow-right">
        <el-breadcrumb-item :to="{ path: '/' }">Homepage</el-breadcrumb-item>
        <el-breadcrumb-item>{{ categoryName }}</el-breadcrumb-item>
        <el-breadcrumb-item>{{ subCategoryName }}</el-breadcrumb-item>
        <el-breadcrumb-item>{{ productName }}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div class="product-overview-body">
      <div class="image-box">
        <img :src="this.imageURL" alt="book" />
      </div>

      <div class="product-overview-body-content">
        <div class="product-name">
          <div class="title">
            <span class="category">{{ categoryName }}</span>
            <span> - </span>
            <span class="content">{{ productName }}</span>
            <span> - </span>
            <span>{{ producer }}</span>
          </div>
        </div>
        <div class="product-id">
          <div class="title">
            Product ID: <span class="content">{{ productNumber }}</span>
          </div>
        </div>
        <div class="rating-box">
          <div class="rating">
            <div class="title">{{ rating }}</div>
            <el-rate v-model="ratingValue" :max="5"></el-rate>
          </div>
        </div>

        <div class="price-box">
          <div class="price">
            <div class="title">
              <span class="content">${{ price }}</span>
            </div>
          </div>
        </div>

        <div class="information-box">
          <div class="row">
            <div class="col">Color</div>
            <div class="col">
              <div class="item-group">
                <div v-if="colorList.length > 0">
                  <item-tag
                    v-for="(color, index) in colorList"
                    :key="index"
                    :content="color"
                  />
                </div>
                <div v-else>Unknown</div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col">Size</div>
            <div class="col">
              <div class="item-group">
                <div v-if="sizeList.length > 0">
                  <item-tag
                    v-for="(size, index) in sizeList"
                    :key="index"
                    :content="size"
                  />
                </div>
                <div v-else>Unknown</div>
              </div>
            </div>
          </div>

          <div class="row">
            <div class="col">Style</div>
            <div class="col">{{ productStyle }}</div>
          </div>

          <div class="row">
            <div class="col">Quantity</div>
            <div class="col">{{ quantity }}</div>
          </div>

          <div class="row">
            <div class="col">Sell Start Date</div>
            <div class="col">{{ sellStartDate }}</div>
          </div>

          <div class="row">
            <div class="col">Sell Start End</div>
            <div class="col">{{ sellEndDate }}</div>
          </div>

          <!-- <div class="button-row">
            <el-button
              type="primary"
              class="direction-btn"
              @click="onClickTransactionDetail"
              >Transactions</el-button
            >
          </div> -->
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
      // colorList: ["Red", "Blue", "Yellow", "Green"],
      // sizeList: ["XS", "S", "M", "L", "XL"],
    };
  },
  components: {
    ItemTag,
  },
  props: {
    productName: {
      type: String,
      default: "Product Name",
    },
    imageURL: {
      type: String,
      default: "./assets/No_Image_Available.jpg",
    },
    productNumber: {
      type: String,
      default: "BOOKGG67GD74H",
    },
    categoryName: {
      type: String,
      default: "Category",
    },
    subCategoryName: {
      type: String,
      default: "Sub Category",
    },
    sellStartDate: {
      type: String,
      default: "14/5/2014",
    },
    sellEndDate: {
      type: String,
      default: "None",
    },
    producer: {
      type: String,
      default: "Nha san xuat",
    },
    price: {
      type: String,
      default: "49.99",
    },
    quantity: {
      type: String,
      default: "5000",
    },
    productStyle: {
      type: String,
      default: "Unknown",
    },
    sizeList: {
      type: Array,
      default: function () {
        return [];
      },
    },
    colorList: {
      type: Array,
      default: function () {
        return [];
      },
    },
    rating: {
      type: Number,
      default: 4.9,
    },
  },
  methods: {
    onClickTransactionDetail() {
      const transaction = {
        productName: "Books",
      };

      this.$router.push(`/transaction/${transaction.productName}`);
    },
  },
  mounted() {},
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

    background-color: $color-white;

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
        .title {
          padding: 10px 0;
        }
      }

      .rating-box {
        .rating {
          color: $color-primary;
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
          background-color: $color-primary;
          border-color: $color-primary;

          &:hover {
            background-color: $color-secondary;
          }
        }
      }
    }
  }
}
</style>