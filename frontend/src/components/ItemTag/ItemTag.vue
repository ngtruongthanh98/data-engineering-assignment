<template>
  <div class="custom-tag">
    <div class="text">{{ content }}</div>
  </div>
</template>

<script>
export default {
  props: {
    content: {
      type: String,
      default: "",
    },
  },
};
</script>

<style lang="scss" scoped>
.custom-tag {
  border: 1px solid rgba(0, 0, 0, 0.09);
  padding: 5px 10px;
  cursor: pointer;

  &:hover {
    color: #ee4d2d;
    border-color: #ee4d2d;
  }

  .text {
    text-align: center;
  }
}
</style>