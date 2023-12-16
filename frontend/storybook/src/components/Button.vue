<template>
  <button :class="classes" @click="onClick" :style="style" :disabled="disabled">
    <my-icon v-if="icon" :name="icon" :size="iconsize" :color="iconcolor" />
    <span v-if="label">{{ label }}</span>
  </button>
</template>

<script>
import MyIcon from "./Icons.vue";

export default {
  name: 'my-button',
  components: { MyIcon },
  props: {
    label: {
      type: String,
      default: '',
    },
    icon: {
      type: String,
      default: '',
    },
    theme: {
      type: String,
      default: 'filled',
      validator: function (value) {
        return ['filled','outline','floating','flat'].indexOf(value) !== -1;
      },
    },
    size: {
      type: String,
      default: 'medium',
      validator: function (value) {
        return ['small','medium','large'].indexOf(value) !== -1;
      },
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },

  computed: {
    classes() {
      return {
        'my-button': true,
        [`my-button--theme-${this.theme}`]: true,
        [`my-button--size-${this.size}`]: true,
        'my-button--icon-only': this.icon && !this.label,
        'my-button--label-only': !this.icon && this.label,
        'my-button--icon-label': this.icon && this.label,
      };
    },
    style() {
      return {
      };
    },
    iconsize() {
      switch (this.size) {
        case 'small':
          return 16;
        case 'medium':
          return 16;
        case 'large':
          return 24;
      }
    },
    iconcolor() {
      switch (this.theme) {
        case 'filled':
          return 'white';
        case 'outline':
          return this.disabled ? 'normal_grey' : 'black';
        case 'floating':
          return 'white';
        case 'flat':
          return this.disabled ? 'normal_grey' : 'black';
      }
    },
  },

  methods: {
    onClick() {
      this.$emit('onClick');
    },
  },
};
</script>

<style scoped lang="scss">
@import 'colors';
@import 'font';

.my-button {
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  vertical-align: middle;

  span {
    margin: 0;
  }
}

.my-button--size {
  &-large {
    padding: 8px 20px;
    font-size: 18px;
    line-height: 32px;
    border-radius: 14px;
  }

  &-medium {
    padding: 6px 18px;
    font-size: 16px;
    line-height: 29px;
    border-radius: 12px;
  }

  &-small {
    padding: 4px 16px;
    font-size: 14px;
    line-height: 25px;
    border-radius: 10px;

    img {
      width: 16px;
      height: 16px;
    }
  }
}

.my-button--icon-only {
  &.my-button--size {
    &-large {
      padding: 12px;
    }

    &-medium {
      padding: 8.5px;
    }

    &-small {
      padding: 8.5px;
    }
  }
}


.my-button--theme-floating {
  &.my-button--size {
    &-large {
      padding: 8px 24px;
      border-radius: 24px;
    }

    &-medium {
      padding: 6px 22px;
      border-radius: 20px;
    }

    &-small {
      padding: 4px 20px;
      border-radius: 16px;
    }
  }
}


.my-button--theme-floating.my-button--icon-only {
  &.my-button--size {
    &-large {
      padding: 12px;
    }

    &-medium {
      padding: 8.5px;
    }

    &-small {
      padding: 8.5px;
    }
  }
}

.my-button--icon-label {
  span {
    margin-left: 12px;
  }
}

.my-button--theme {
  &-filled {
    background-color: $bricks_red;
    border: 0;

    span {
      color: $white;
    }

    &:hover {
      background-color: $red400;
    }

    &:active {
      background-color: $red700;
    }

    &:focus:not(:active) {
      box-shadow: 0px 4px 8px 0px #00000066;
    }

    &:disabled {
      background-color: $normal_grey;
    }
  }

  &-outline {
    background-color: $white;
    border: 1px solid $red1000;

    &:hover {
      background-color: $light_grey;
    }

    &:active {
      background-color: $red200;
      border: 1.5px solid $red1000;
    }

    &:focus:not(:active) {
      background-color: $white;
      border: 1px solid $bricks_red;
    }

    &:disabled {
      border: 1px solid $normal_grey;
      background-color: $white;
      color: $normal_grey;
    }
  }

  &-flat {
    @extend .my-button--theme-outline;
    border: none;

    &:active {
      border: none;
    }

    &:focus:not(:active) {
      border: 1px solid $bricks_red;
    }

    &:disabled {
      border: none;
    }
  }

  &-floating {
    @extend .my-button--theme-filled;
    box-shadow: 0px 4px 8px 0px #00000066;
  }
}</style>