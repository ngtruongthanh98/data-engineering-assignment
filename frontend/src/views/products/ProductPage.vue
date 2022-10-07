<template>
  <div class="product-page">
    <header-component />
    <h1>Category</h1>

    <div class="product-page-body">
      <div class="category-container">
        <!-- <div class="row">
          <div class="col">
            <div class="category-item">
              <img
                src="https://cf.shopee.vn/file/687f3967b7c2fe6a134a2c11894eea4b_tn"
                alt=""
                class="image"
              />
              <div class="title">Men Clothes</div>
            </div>

            <div class="category-item">
              <img
                src="https://cf.shopee.vn/file/687f3967b7c2fe6a134a2c11894eea4b_tn"
                alt=""
                class="image"
              />
              <div class="title">Men Clothes</div>
            </div>
          </div>
        </div> -->

        <div
          v-for="(categoryItem, index) in categoryList"
          :key="index"
          class="category-item"
        >
          <img :src="categoryItem.image" alt="" class="image" />
          <div class="title">{{ categoryItem.title }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import { categoryList } from "@/constants";

export default {
  name: "ProductPage",
  data: function () {
    return {
      categoryList,
    };
  },
  components: {
    HeaderComponent,
  },
};
</script>

<style lang="scss" scoped>
.product-page {
  &-body {
    margin: 0px 200px 0px 200px;

    .category-container {
      display: grid;
      grid-auto-flow: column dense; /* column flow with "dense" to fill all the cells */
      grid-template-rows: 150px 150px; /* 2 rows */
      grid-auto-columns: 120px;
      justify-content: center;

      .category-item {
        transition: opacity 0.2s ease;
        border: 1px solid rgba(0, 0, 0, 0.05);

        &:hover {
          border: 2px solid rgba(0, 0, 0, 0.05);
          cursor: pointer;
        }

        .image {
          width: 100px;
          height: 100px;
        }

        .title {
        }
      }
    }
  }
}
</style>
