<template>
  <div class="product-rating">
    <div class="product-rating-body">
      <div class="title">Product Ratings</div>

      <div class="rating-overview-box">
        <div class="star-box">
          <span class="star">{{ overviewStar }}</span> out of 5
          <el-rate v-model="overviewStar" :max="5"></el-rate>
        </div>

        <div class="star-detail-box">
          <item-tag
            v-for="(starTagDataItem, index) in starTagData"
            :key="index"
            :content="starTagDataItem"
            class="custom-item-tag"
          />
        </div>
      </div>

      <div class="comment-box">
        <div
          v-for="(usersDataItem, index) in usersData"
          :key="index"
          class="comment-box-item"
        >
          <user-avatar />

          <div class="comment-information">
            <div class="reviewer-name">
              {{ usersDataItem.reviewerName }}
              <span class="email">({{ usersDataItem.emailAddress }})</span>
            </div>
            <el-rate v-model="overviewStar" :max="5"></el-rate>
            <div class="review-date">{{ usersDataItem.reviewerData }}</div>
            <div class="comment">
              {{ usersDataItem.comment }}
            </div>
          </div>
        </div>

        <el-pagination
          class="pagination-box"
          small
          layout="prev, pager, next"
          :total="50"
        >
        </el-pagination>
      </div>
    </div>
  </div>
</template>

<script>
import UserAvatar from "@/components/UserAvatar/UserAvatar";
import ItemTag from "@/components/ItemTag/ItemTag";
export default {
  data() {
    return {
      overviewStar: 4.9,
      usersData: [
        {
          reviewerName: "tramgnguyenjin",
          reviewerData: "2022-09-02 22:33",
          emailAddress: "tramgnguyenjin@gmail.com",
          rating: "5",
          comment:
            "Đọc thì hay nhưng cái này dành cho ng đi làm sẽ phù hợp hơn và so sánh sau một chương sẽ có một phần để tóm tắt lại",
          modifiedDate: "",
        },
        {
          reviewerName: "tramgnguyenjin",
          reviewerData: "2022-09-02 22:33",
          emailAddress: "tramgnguyenjin@gmail.com",
          rating: "5",
          comment: "tramgnguyenjin",
          modifiedDate: "",
        },
        {
          reviewerName: "tramgnguyenjin",
          reviewerData: "2022-09-02 22:33",
          emailAddress: "tramgnguyenjin@gmail.com",
          rating: "5",
          comment: "tramgnguyenjin",
          modifiedDate: "",
        },
        {
          reviewerName: "tramgnguyenjin",
          reviewerData: "2022-09-02 22:33",
          emailAddress: "tramgnguyenjin@gmail.com",
          rating: "5",
          comment: "tramgnguyenjin",
          modifiedDate: "",
        },
      ],
      starTagData: ["All", "5 Star", "4 Star", "3 Star", "2 Star", "1 Star"],
    };
  },
  components: {
    UserAvatar,
    ItemTag,
  },
};
</script>

<style lang="scss">
.product-rating {
  padding: 24px 200px 0px 200px;

  &-body {
    background-color: white;
    text-align: start;
    padding-bottom: 24px;

    .title {
      font-size: 18px;
      padding: 24px;
      text-align: start;
    }

    .rating-overview-box {
      margin: 24px;
      padding: 24px;

      border: 1px solid $color-border;
      background-color: $color-background;

      display: grid;
      grid-template-columns: 200px 1fr;

      .star-box {
        color: $color-tertiary;
        font-size: 18px;

        .star {
          font-size: 1.875rem;
        }

        .el-rate__icon {
          font-size: 24px;
        }
      }

      .star-detail-box {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr;
        gap: 10px;

        .custom-item-tag {
          height: 2rem;
          line-height: 2rem;
          border-radius: 2px;
          margin-bottom: 0.3125rem;
          margin-top: 0.3125rem;
        }
      }
    }

    .comment-box {
      margin-left: 24px;

      &-item {
        display: flex;
        padding: 1rem 1rem 1rem 1.25rem;
        margin-right: 1rem;
        border-bottom: 1px solid $color-border-tag;

        .user-avatar {
          margin-right: 10px;
        }

        .comment-information {
          .reviewer-name {
            .email {
              font-style: italic;
            }
          }

          .review-date {
            margin-top: 24px;
          }

          .comment {
            margin-top: 12px;
          }
        }
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