<!-- eslint-disable vue/multi-word-component-names -->
<template>
  <div class="category">
    <header-component />

    <sub-category-component
      :title="categoryName"
      :subCategoryList="subCategoryList"
    />
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import SubCategoryComponent from "@/views/category/SubCategoryComponent";
import { getSubCategories } from "@/services/products";

export default {
  data() {
    return {
      subCategoryList: [],
      categoryName: "",
    };
  },
  components: {
    HeaderComponent,
    SubCategoryComponent,
  },
  methods: {
    async getSubCategories() {
      const queryParams = {
        CategoryName: this.categoryName,
      };
      const response = await getSubCategories(queryParams);
      this.subCategoryList = response.data.data.map((item) => {
        return {
          subcategoryName: item.subcategoryName,
        };
      });
    },
  },
  mounted() {
    this.categoryName = decodeURIComponent(this.$route.path.split("/")[3]);
    this.getSubCategories(this.categoryName);
  },
};
</script>

<style lang="scss">
.category {
}
</style>