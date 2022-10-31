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
  border: 1px solid $color-border-tag;
  padding: 5px 10px;
  cursor: pointer;

  &:hover {
    color: $color-primary;
    border-color: $color-primary;
  }

  .text {
    text-align: center;
  }
}
</style>