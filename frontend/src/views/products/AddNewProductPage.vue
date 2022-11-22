<template>
  <div class="add-new-product-page">
    <header-component />
    <div class="add-new-product-page__body">
      <div class="title">Add new product</div>

      <!-- label -->

      <div class="input-container">
        <div class="input-element">
          <div class="label">Product name</div>
          <el-input
            placeholder="Enter product name"
            v-model="inputProductName"
            class="input"
          ></el-input>
        </div>

        <!-- product id -->
        <div class="input-element">
          <div class="label">Product ID</div>
          <el-input
            placeholder="Enter product ID"
            v-model="inputProductId"
            class="input"
          ></el-input>
        </div>

        <!-- product category -->
        <div class="input-element">
          <div class="label">Product category</div>
          <el-input
            placeholder="Enter product category"
            v-model="inputProductCategory"
            class="input"
          ></el-input>
        </div>

        <!-- product subcategory -->
        <div class="input-element">
          <div class="label">Product subcategory</div>
          <el-input
            placeholder="Enter product subcategory"
            v-model="inputProductSubcategory"
            class="input"
          ></el-input>
        </div>

        <!-- product price -->
        <div class="input-element">
          <div class="label">Product price</div>
          <el-input
            placeholder="Enter product price"
            v-model="inputProductPrice"
            class="input"
          ></el-input>
        </div>

        <!-- product image url -->
        <div class="input-element">
          <div class="label">Product image url</div>
          <el-input
            placeholder="Enter product image url"
            v-model="inputProductImageUrl"
            class="input"
          ></el-input>
        </div>

        <!-- product brand -->
        <div class="input-element">
          <div class="label">Product brand</div>
          <el-input
            placeholder="Enter product brand"
            v-model="inputProductBrand"
            class="input"
          ></el-input>
        </div>

        <!-- rating -->
        <div class="input-element">
          <div class="label">Rating</div>
          <el-input
            placeholder="Enter rating"
            v-model="inputRating"
            class="input"
          ></el-input>
        </div>
      </div>

      <el-button type="primary" @click="addNewProduct">Submit</el-button>
    </div>
  </div>
</template>

<script>
import HeaderComponent from "@/components/Header/HeaderComponent";
import { createProduct } from "@/services/products";

export default {
  data() {
    return {
      inputProductName: "",
      inputProductId: "",
      inputProductCategory: "",
      inputProductSubcategory: "",
      inputProductPrice: "",
      inputProductImageUrl: "",
      inputProductBrand: "",
      inputRating: "",
    };
  },
  components: {
    HeaderComponent,
  },
  methods: {
    async createProduct(queryParams) {
      try {
        const response = await createProduct(queryParams);
        console.log(response);

        //clear input
        this.inputProductName = "";
        this.inputProductId = "";
        this.inputProductCategory = "";
        this.inputProductSubcategory = "";
        this.inputProductPrice = "";
        this.inputProductImageUrl = "";
        this.inputProductBrand = "";
        this.inputRating = "";
      } catch (error) {
        console.log(error);
      }
    },
    addNewProduct() {
      if (this.inputProductName === "" || this.inputProductSubcategory === "") {
        alert("Please fill product name and product subcategory");
        return;
      }

      // call API create product
      const queryParams = {
        productName: this.inputProductName,
        productID: this.inputProductId,
        categoryName: this.inputProductCategory,
        subcategoryName: this.inputProductSubcategory,
        standardCost: this.inputProductPrice,
        categoryImage: this.inputProductImageUrl,
        identityItemBrand: this.inputProductBrand,
        rating: this.inputRating,
      };

      this.createProduct(queryParams);

      // clear input
      this.inputProductName = "";
      this.inputProductId = "";
      this.inputProductCategory = "";
      this.inputProductSubcategory = "";
      this.inputProductPrice = "";
      this.inputProductImageUrl = "";
      this.inputProductBrand = "";
      this.inputRating = "";
    },
  },
};
</script>

<style lang="scss">
.add-new-product-page {
  &__body {
    margin: 40px 200px 0px 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;

    .title {
      font-size: 24px;
      font-weight: 600;
      margin-bottom: 40px;
    }

    .input-container {
      margin-bottom: 20px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-gap: 20px;

      .input-element {
        display: flex;
        flex-direction: column;
        align-items: start;

        .label {
          font-size: 16px;
          font-weight: 600;
          margin-bottom: 10px;
        }

        .input {
          width: 400px;
          margin-bottom: 20px;
        }
      }
    }
  }
}
</style>