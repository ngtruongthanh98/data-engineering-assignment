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
// import { HOME_APPLIANCES } from "@/constants";
import { getSubCategories } from "@/services/products";

export default {
  data() {
    return {
      // subCategoryList: HOME_APPLIANCES,
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
      console.log("response: ", response);
      // this.subCategoryList = response.data.data;

      // map response.data.data
      this.subCategoryList = response.data.data.map((item) => {
        return {
          subcategoryName: item.subcategoryName,
        };
      });

      console.log("subCategoryList: ", this.subCategoryList);
    },
  },
  mounted() {
    this.categoryName = decodeURIComponent(this.$route.path.split("/")[1]);
    this.getSubCategories(this.categoryName);
  },
};
</script>

<style lang="scss">
.category {
}
</style>