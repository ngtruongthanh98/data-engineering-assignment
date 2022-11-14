<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="sub-category-container">
    <h1 class="title">{{ title }}</h1>

    <div class="body">
      <sub-category-list
        :title="title"
        :subCategoryList="subCategoryList"
        @select-subcategory="handleSelectSubCategory"
      />
      <div class="main">
        <div class="product-item-container">
          <product-item
            v-for="(product, index) in productList"
            :key="index"
            :product-data-overview="product"
          />
        </div>

        <!-- <el-pagination
          class="pagination-box"
          small
          layout="prev, pager, next"
          :total="50"
        >
        </el-pagination> -->
      </div>
    </div>
  </div>
</template>

<script>
import SubCategoryList from "./SubCategoryList";
import ProductItem from "./ProductItem";
import { getProducts } from "@/services/products";

export default {
  data() {
    return {
      productList: [],
      SubcategoryName: "",
    };
  },
  props: {
    title: {
      type: String,
      default: "",
    },
    subCategoryList: {
      type: Array,
      default: () => [],
    },
  },
  components: {
    SubCategoryList,
    ProductItem,
  },
  watch: {
    SubcategoryName() {
      this.getProducts();
    },
  },
  methods: {
    async getProducts() {
      const queryParams = {
        SubcategoryName: this.SubcategoryName || "Baby & Child Care",
      };
      const response = await getProducts(queryParams);
      this.productList = response.data.data;
    },
    handleSelectSubCategory(SubcategoryName) {
      this.SubcategoryName = SubcategoryName;
    },
  },
  mounted() {
    this.getProducts();
  },
};
</script>

<style lang="scss">
.sub-category-container {
  .title {
    padding: 24px;
    font-size: 18px;
  }
  .body {
    font-size: 14px;
    display: flex;
    margin: 0px 200px 0px 200px;

    .sub-category-list {
      width: 20%;
    }

    .main {
      .product-item-container {
        width: 80%;
        display: grid;
        grid-template-columns: repeat(5, 230px);
        gap: 10px;
        height: 80vh;
      }

      .pagination-box {
        text-align: end;
        margin-top: 24px;
        margin-right: 1rem;

        .el-pager li.active {
          color: $color-tertiary;
        }

        .el-pager li {
          &:hover {
            color: $color-tertiary;
          }
        }

        .btn-prev,
        .btn-next {
          &:hover {
            color: $color-tertiary;
          }
        }
      }
    }
  }
}
</style>