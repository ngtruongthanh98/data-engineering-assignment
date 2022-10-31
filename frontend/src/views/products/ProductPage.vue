<template>
  <div class="product-page">
    <header-component />
    <div class="category-title">Category</div>

    <div class="product-page-body">
      <div class="category-container">
        <div
          v-for="(categoryItem, index) in categoryList"
          :key="index"
          class="category-item"
          @click="onHandleClick(categoryItem.link)"
        >
          <img :src="categoryItem.image" alt="" class="image" />
          <div class="title">{{ categoryItem.title }}</div>
        </div>
      </div>
    </div>

    <copyright />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import Copyright from "@/components/Copyright";
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
    Copyright,
  },
  methods: {
    onHandleClick(link) {
      this.$router.push(`/${link}`);
    },
  },
};
</script>

<style lang="scss" scoped>
.product-page {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;

  .category-title {
    padding: 24px;
    font-size: 24px;
  }

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
