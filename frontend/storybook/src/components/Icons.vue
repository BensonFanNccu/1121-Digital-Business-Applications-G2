<template>
  <component :style="style" :is="dynamicComponent" />
</template>

<script>
import { Colors,ColorsArray } from "./Colors.js";
import IconActivity from "../IconsComponent/activity.vue";
import IconAirplay from "../IconsComponent/airplay.vue";
import IconAlertCircle from "../IconsComponent/alert-circle.vue";
import IconAlertOctagon from "../IconsComponent/alert-octagon.vue";
import IconAlertTriangle from "../IconsComponent/alert-triangle.vue";
import IconAlignCenter from "../IconsComponent/align-center.vue";
import IconAlignJustify from "../IconsComponent/align-justify.vue";
import IconAlignLeft from "../IconsComponent/align-left.vue";
import IconAlignRight from "../IconsComponent/align-right.vue";
import IconAnchor from "../IconsComponent/anchor.vue";
import IconAperture from "../IconsComponent/aperture.vue";
import IconArchive from "../IconsComponent/archive.vue";
import IconArrowDownCircle from "../IconsComponent/arrow-down-circle.vue";
import IconArrowDownLeft from "../IconsComponent/arrow-down-left.vue";
import IconArrowDownRight from "../IconsComponent/arrow-down-right.vue";
import IconArrowDown from "../IconsComponent/arrow-down.vue";
import IconArrowLeftCircle from "../IconsComponent/arrow-left-circle.vue";
import IconArrowLeft from "../IconsComponent/arrow-left.vue";
import IconArrowRightCircle from "../IconsComponent/arrow-right-circle.vue";
import IconArrowRight from "../IconsComponent/arrow-right.vue";
import IconArrowUpCircle from "../IconsComponent/arrow-up-circle.vue";
import IconArrowUpLeft from "../IconsComponent/arrow-up-left.vue";
import IconArrowUpRight from "../IconsComponent/arrow-up-right.vue";
import IconArrowUp from "../IconsComponent/arrow-up.vue";
import IconAtSign from "../IconsComponent/at-sign.vue";
import IconAward from "../IconsComponent/award.vue";
import IconBarChart2 from "../IconsComponent/bar-chart-2.vue";
import IconBarChart from "../IconsComponent/bar-chart.vue";
import IconBatteryCharging from "../IconsComponent/battery-charging.vue";
import IconBattery from "../IconsComponent/battery.vue";
import IconBellOff from "../IconsComponent/bell-off.vue";
import IconBell from "../IconsComponent/bell.vue";
import IconBluetooth from "../IconsComponent/bluetooth.vue";
import IconBold from "../IconsComponent/bold.vue";
import IconBookOpen from "../IconsComponent/book-open.vue";
import IconBook from "../IconsComponent/book.vue";
import IconBookmark from "../IconsComponent/bookmark.vue";
import IconBox from "../IconsComponent/box.vue";
import IconBriefcase from "../IconsComponent/briefcase.vue";
import IconCalendar from "../IconsComponent/calendar.vue";
import IconCameraOff from "../IconsComponent/camera-off.vue";
import IconCamera from "../IconsComponent/camera.vue";
import IconCast from "../IconsComponent/cast.vue";
import IconCheckCircle from "../IconsComponent/check-circle.vue";
import IconCheckSquare from "../IconsComponent/check-square.vue";
import IconCheck from "../IconsComponent/check.vue";
import IconChevronDown from "../IconsComponent/chevron-down.vue";
import IconChevronLeft from "../IconsComponent/chevron-left.vue";
import IconChevronRight from "../IconsComponent/chevron-right.vue";
import IconChevronUp from "../IconsComponent/chevron-up.vue";
import IconChevronsDown from "../IconsComponent/chevrons-down.vue";
import IconChevronsLeft from "../IconsComponent/chevrons-left.vue";
import IconChevronsRight from "../IconsComponent/chevrons-right.vue";
import IconChevronsUp from "../IconsComponent/chevrons-up.vue";
import IconChrome from "../IconsComponent/chrome.vue";
import IconCircle from "../IconsComponent/circle.vue";
import IconClipboard from "../IconsComponent/clipboard.vue";
import IconClock from "../IconsComponent/clock.vue";
import IconCloudDrizzle from "../IconsComponent/cloud-drizzle.vue";
import IconCloudLightning from "../IconsComponent/cloud-lightning.vue";
import IconCloudOff from "../IconsComponent/cloud-off.vue";
import IconCloudRain from "../IconsComponent/cloud-rain.vue";
import IconCloudSnow from "../IconsComponent/cloud-snow.vue";
import IconCloud from "../IconsComponent/cloud.vue";
import IconCode from "../IconsComponent/code.vue";
import IconCodepen from "../IconsComponent/codepen.vue";
import IconCodesandbox from "../IconsComponent/codesandbox.vue";
import IconCoffee from "../IconsComponent/coffee.vue";
import IconColumns from "../IconsComponent/columns.vue";
import IconCommand from "../IconsComponent/command.vue";
import IconCompass from "../IconsComponent/compass.vue";
import IconCopy from "../IconsComponent/copy.vue";
import IconCornerDownLeft from "../IconsComponent/corner-down-left.vue";
import IconCornerDownRight from "../IconsComponent/corner-down-right.vue";
import IconCornerLeftDown from "../IconsComponent/corner-left-down.vue";
import IconCornerLeftUp from "../IconsComponent/corner-left-up.vue";
import IconCornerRightDown from "../IconsComponent/corner-right-down.vue";
import IconCornerRightUp from "../IconsComponent/corner-right-up.vue";
import IconCornerUpLeft from "../IconsComponent/corner-up-left.vue";
import IconCornerUpRight from "../IconsComponent/corner-up-right.vue";
import IconCpu from "../IconsComponent/cpu.vue";
import IconCreditCard from "../IconsComponent/credit-card.vue";
import IconCrop from "../IconsComponent/crop.vue";
import IconCrosshair from "../IconsComponent/crosshair.vue";
import IconDatabase from "../IconsComponent/database.vue";
import IconDelete from "../IconsComponent/delete.vue";
import IconDisc from "../IconsComponent/disc.vue";
import IconDivideCircle from "../IconsComponent/divide-circle.vue";
import IconDivideSquare from "../IconsComponent/divide-square.vue";
import IconDivide from "../IconsComponent/divide.vue";
import IconDollarSign from "../IconsComponent/dollar-sign.vue";
import IconDownloadCloud from "../IconsComponent/download-cloud.vue";
import IconDownload from "../IconsComponent/download.vue";
import IconDribbble from "../IconsComponent/dribbble.vue";
import IconDroplet from "../IconsComponent/droplet.vue";
import IconEdit2 from "../IconsComponent/edit-2.vue";
import IconEdit3 from "../IconsComponent/edit-3.vue";
import IconEdit from "../IconsComponent/edit.vue";
import IconExternalLink from "../IconsComponent/external-link.vue";
import IconEyeOff from "../IconsComponent/eye-off.vue";
import IconEye from "../IconsComponent/eye.vue";
import IconFacebook from "../IconsComponent/facebook.vue";
import IconFastForward from "../IconsComponent/fast-forward.vue";
import IconFeather from "../IconsComponent/feather.vue";
import IconFigma from "../IconsComponent/figma.vue";
import IconFileMinus from "../IconsComponent/file-minus.vue";
import IconFilePlus from "../IconsComponent/file-plus.vue";
import IconFileText from "../IconsComponent/file-text.vue";
import IconFile from "../IconsComponent/file.vue";
import IconFilm from "../IconsComponent/film.vue";
import IconFilter from "../IconsComponent/filter.vue";
import IconFlag from "../IconsComponent/flag.vue";
import IconFolderMinus from "../IconsComponent/folder-minus.vue";
import IconFolderPlus from "../IconsComponent/folder-plus.vue";
import IconFolder from "../IconsComponent/folder.vue";
import IconFramer from "../IconsComponent/framer.vue";
import IconFrown from "../IconsComponent/frown.vue";
import IconGift from "../IconsComponent/gift.vue";
import IconGitBranch from "../IconsComponent/git-branch.vue";
import IconGitCommit from "../IconsComponent/git-commit.vue";
import IconGitMerge from "../IconsComponent/git-merge.vue";
import IconGitPullRequest from "../IconsComponent/git-pull-request.vue";
import IconGithub from "../IconsComponent/github.vue";
import IconGitlab from "../IconsComponent/gitlab.vue";
import IconGlobe from "../IconsComponent/globe.vue";
import IconGrid from "../IconsComponent/grid.vue";
import IconHardDrive from "../IconsComponent/hard-drive.vue";
import IconHash from "../IconsComponent/hash.vue";
import IconHeadphones from "../IconsComponent/headphones.vue";
import IconHeart from "../IconsComponent/heart.vue";
import IconHelpCircle from "../IconsComponent/help-circle.vue";
import IconHexagon from "../IconsComponent/hexagon.vue";
import IconHome from "../IconsComponent/home.vue";
import IconImage from "../IconsComponent/image.vue";
import IconInbox from "../IconsComponent/inbox.vue";
import IconInfo from "../IconsComponent/info.vue";
import IconInstagram from "../IconsComponent/instagram.vue";
import IconItalic from "../IconsComponent/italic.vue";
import IconKey from "../IconsComponent/key.vue";
import IconLayers from "../IconsComponent/layers.vue";
import IconLayout from "../IconsComponent/layout.vue";
import IconLifeBuoy from "../IconsComponent/life-buoy.vue";
import IconLink2 from "../IconsComponent/link-2.vue";
import IconLink from "../IconsComponent/link.vue";
import IconLinkedin from "../IconsComponent/linkedin.vue";
import IconList from "../IconsComponent/list.vue";
import IconLoader from "../IconsComponent/loader.vue";
import IconLock from "../IconsComponent/lock.vue";
import IconLogIn from "../IconsComponent/log-in.vue";
import IconLogOut from "../IconsComponent/log-out.vue";
import IconMail from "../IconsComponent/mail.vue";
import IconMapPin from "../IconsComponent/map-pin.vue";
import IconMap from "../IconsComponent/map.vue";
import IconMaximize2 from "../IconsComponent/maximize-2.vue";
import IconMaximize from "../IconsComponent/maximize.vue";
import IconMeh from "../IconsComponent/meh.vue";
import IconMenu from "../IconsComponent/menu.vue";
import IconMessageCircle from "../IconsComponent/message-circle.vue";
import IconMessageSquare from "../IconsComponent/message-square.vue";
import IconMicOff from "../IconsComponent/mic-off.vue";
import IconMic from "../IconsComponent/mic.vue";
import IconMinimize2 from "../IconsComponent/minimize-2.vue";
import IconMinimize from "../IconsComponent/minimize.vue";
import IconMinusCircle from "../IconsComponent/minus-circle.vue";
import IconMinusSquare from "../IconsComponent/minus-square.vue";
import IconMinus from "../IconsComponent/minus.vue";
import IconMonitor from "../IconsComponent/monitor.vue";
import IconMoon from "../IconsComponent/moon.vue";
import IconMoreHorizontal from "../IconsComponent/more-horizontal.vue";
import IconMoreVertical from "../IconsComponent/more-vertical.vue";
import IconMousePointer from "../IconsComponent/mouse-pointer.vue";
import IconMove from "../IconsComponent/move.vue";
import IconMusic from "../IconsComponent/music.vue";
import IconNavigation2 from "../IconsComponent/navigation-2.vue";
import IconNavigation from "../IconsComponent/navigation.vue";
import IconOctagon from "../IconsComponent/octagon.vue";
import IconPackage from "../IconsComponent/package.vue";
import IconPaperclip from "../IconsComponent/paperclip.vue";
import IconPauseCircle from "../IconsComponent/pause-circle.vue";
import IconPause from "../IconsComponent/pause.vue";
import IconPenTool from "../IconsComponent/pen-tool.vue";
import IconPercent from "../IconsComponent/percent.vue";
import IconPhoneCall from "../IconsComponent/phone-call.vue";
import IconPhoneForwarded from "../IconsComponent/phone-forwarded.vue";
import IconPhoneIncoming from "../IconsComponent/phone-incoming.vue";
import IconPhoneMissed from "../IconsComponent/phone-missed.vue";
import IconPhoneOff from "../IconsComponent/phone-off.vue";
import IconPhoneOutgoing from "../IconsComponent/phone-outgoing.vue";
import IconPhone from "../IconsComponent/phone.vue";
import IconPieChart from "../IconsComponent/pie-chart.vue";
import IconPlayCircle from "../IconsComponent/play-circle.vue";
import IconPlay from "../IconsComponent/play.vue";
import IconPlusCircle from "../IconsComponent/plus-circle.vue";
import IconPlusSquare from "../IconsComponent/plus-square.vue";
import IconPlus from "../IconsComponent/plus.vue";
import IconPocket from "../IconsComponent/pocket.vue";
import IconPower from "../IconsComponent/power.vue";
import IconPrinter from "../IconsComponent/printer.vue";
import IconRadio from "../IconsComponent/radio.vue";
import IconRefreshCcw from "../IconsComponent/refresh-ccw.vue";
import IconRefreshCw from "../IconsComponent/refresh-cw.vue";
import IconRepeat from "../IconsComponent/repeat.vue";
import IconRewind from "../IconsComponent/rewind.vue";
import IconRotateCcw from "../IconsComponent/rotate-ccw.vue";
import IconRotateCw from "../IconsComponent/rotate-cw.vue";
import IconRss from "../IconsComponent/rss.vue";
import IconSave from "../IconsComponent/save.vue";
import IconScissors from "../IconsComponent/scissors.vue";
import IconSearch from "../IconsComponent/search.vue";
import IconSend from "../IconsComponent/send.vue";
import IconServer from "../IconsComponent/server.vue";
import IconSettings from "../IconsComponent/settings.vue";
import IconShare2 from "../IconsComponent/share-2.vue";
import IconShare from "../IconsComponent/share.vue";
import IconShieldOff from "../IconsComponent/shield-off.vue";
import IconShield from "../IconsComponent/shield.vue";
import IconShoppingBag from "../IconsComponent/shopping-bag.vue";
import IconShoppingCart from "../IconsComponent/shopping-cart.vue";
import IconShuffle from "../IconsComponent/shuffle.vue";
import IconSidebar from "../IconsComponent/sidebar.vue";
import IconSkipBack from "../IconsComponent/skip-back.vue";
import IconSkipForward from "../IconsComponent/skip-forward.vue";
import IconSlack from "../IconsComponent/slack.vue";
import IconSlash from "../IconsComponent/slash.vue";
import IconSliders from "../IconsComponent/sliders.vue";
import IconSmartphone from "../IconsComponent/smartphone.vue";
import IconSmile from "../IconsComponent/smile.vue";
import IconSpeaker from "../IconsComponent/speaker.vue";
import IconSquare from "../IconsComponent/square.vue";
import IconStar from "../IconsComponent/star.vue";
import IconStopCircle from "../IconsComponent/stop-circle.vue";
import IconSun from "../IconsComponent/sun.vue";
import IconSunrise from "../IconsComponent/sunrise.vue";
import IconSunset from "../IconsComponent/sunset.vue";
import IconTable from "../IconsComponent/table.vue";
import IconTablet from "../IconsComponent/tablet.vue";
import IconTag from "../IconsComponent/tag.vue";
import IconTarget from "../IconsComponent/target.vue";
import IconTerminal from "../IconsComponent/terminal.vue";
import IconThermometer from "../IconsComponent/thermometer.vue";
import IconThumbsDown from "../IconsComponent/thumbs-down.vue";
import IconThumbsUp from "../IconsComponent/thumbs-up.vue";
import IconToggleLeft from "../IconsComponent/toggle-left.vue";
import IconToggleRight from "../IconsComponent/toggle-right.vue";
import IconTool from "../IconsComponent/tool.vue";
import IconTrash2 from "../IconsComponent/trash-2.vue";
import IconTrash from "../IconsComponent/trash.vue";
import IconTrello from "../IconsComponent/trello.vue";
import IconTrendingDown from "../IconsComponent/trending-down.vue";
import IconTrendingUp from "../IconsComponent/trending-up.vue";
import IconTriangle from "../IconsComponent/triangle.vue";
import IconTruck from "../IconsComponent/truck.vue";
import IconTv from "../IconsComponent/tv.vue";
import IconTwitch from "../IconsComponent/twitch.vue";
import IconTwitter from "../IconsComponent/twitter.vue";
import IconType from "../IconsComponent/type.vue";
import IconUmbrella from "../IconsComponent/umbrella.vue";
import IconUnderline from "../IconsComponent/underline.vue";
import IconUnlock from "../IconsComponent/unlock.vue";
import IconUploadCloud from "../IconsComponent/upload-cloud.vue";
import IconUpload from "../IconsComponent/upload.vue";
import IconUserCheck from "../IconsComponent/user-check.vue";
import IconUserMinus from "../IconsComponent/user-minus.vue";
import IconUserPlus from "../IconsComponent/user-plus.vue";
import IconUserX from "../IconsComponent/user-x.vue";
import IconUser from "../IconsComponent/user.vue";
import IconUsers from "../IconsComponent/users.vue";
import IconVideoOff from "../IconsComponent/video-off.vue";
import IconVideo from "../IconsComponent/video.vue";
import IconVoicemail from "../IconsComponent/voicemail.vue";
import IconVolume1 from "../IconsComponent/volume-1.vue";
import IconVolume2 from "../IconsComponent/volume-2.vue";
import IconVolumeX from "../IconsComponent/volume-x.vue";
import IconVolume from "../IconsComponent/volume.vue";
import IconWatch from "../IconsComponent/watch.vue";
import IconWifiOff from "../IconsComponent/wifi-off.vue";
import IconWifi from "../IconsComponent/wifi.vue";
import IconWind from "../IconsComponent/wind.vue";
import IconXCircle from "../IconsComponent/x-circle.vue";
import IconXOctagon from "../IconsComponent/x-octagon.vue";
import IconXSquare from "../IconsComponent/x-square.vue";
import IconX from "../IconsComponent/x.vue";
import IconYoutube from "../IconsComponent/youtube.vue";
import IconZapOff from "../IconsComponent/zap-off.vue";
import IconZap from "../IconsComponent/zap.vue";
import IconZoomIn from "../IconsComponent/zoom-in.vue";
import IconZoomOut from "../IconsComponent/zoom-out.vue";

export default {
  name: "my-icon",
  components: {
    IconActivity,
    IconAirplay,
    IconAlertCircle,
    IconAlertOctagon,
    IconAlertTriangle,
    IconAlignCenter,
    IconAlignJustify,
    IconAlignLeft,
    IconAlignRight,
    IconAnchor,
    IconAperture,
    IconArchive,
    IconArrowDownCircle,
    IconArrowDownLeft,
    IconArrowDownRight,
    IconArrowDown,
    IconArrowLeftCircle,
    IconArrowLeft,
    IconArrowRightCircle,
    IconArrowRight,
    IconArrowUpCircle,
    IconArrowUpLeft,
    IconArrowUpRight,
    IconArrowUp,
    IconAtSign,
    IconAward,
    IconBarChart2,
    IconBarChart,
    IconBatteryCharging,
    IconBattery,
    IconBellOff,
    IconBell,
    IconBluetooth,
    IconBold,
    IconBookOpen,
    IconBook,
    IconBookmark,
    IconBox,
    IconBriefcase,
    IconCalendar,
    IconCameraOff,
    IconCamera,
    IconCast,
    IconCheckCircle,
    IconCheckSquare,
    IconCheck,
    IconChevronDown,
    IconChevronLeft,
    IconChevronRight,
    IconChevronUp,
    IconChevronsDown,
    IconChevronsLeft,
    IconChevronsRight,
    IconChevronsUp,
    IconChrome,
    IconCircle,
    IconClipboard,
    IconClock,
    IconCloudDrizzle,
    IconCloudLightning,
    IconCloudOff,
    IconCloudRain,
    IconCloudSnow,
    IconCloud,
    IconCode,
    IconCodepen,
    IconCodesandbox,
    IconCoffee,
    IconColumns,
    IconCommand,
    IconCompass,
    IconCopy,
    IconCornerDownLeft,
    IconCornerDownRight,
    IconCornerLeftDown,
    IconCornerLeftUp,
    IconCornerRightDown,
    IconCornerRightUp,
    IconCornerUpLeft,
    IconCornerUpRight,
    IconCpu,
    IconCreditCard,
    IconCrop,
    IconCrosshair,
    IconDatabase,
    IconDelete,
    IconDisc,
    IconDivideCircle,
    IconDivideSquare,
    IconDivide,
    IconDollarSign,
    IconDownloadCloud,
    IconDownload,
    IconDribbble,
    IconDroplet,
    IconEdit2,
    IconEdit3,
    IconEdit,
    IconExternalLink,
    IconEyeOff,
    IconEye,
    IconFacebook,
    IconFastForward,
    IconFeather,
    IconFigma,
    IconFileMinus,
    IconFilePlus,
    IconFileText,
    IconFile,
    IconFilm,
    IconFilter,
    IconFlag,
    IconFolderMinus,
    IconFolderPlus,
    IconFolder,
    IconFramer,
    IconFrown,
    IconGift,
    IconGitBranch,
    IconGitCommit,
    IconGitMerge,
    IconGitPullRequest,
    IconGithub,
    IconGitlab,
    IconGlobe,
    IconGrid,
    IconHardDrive,
    IconHash,
    IconHeadphones,
    IconHeart,
    IconHelpCircle,
    IconHexagon,
    IconHome,
    IconImage,
    IconInbox,
    IconInfo,
    IconInstagram,
    IconItalic,
    IconKey,
    IconLayers,
    IconLayout,
    IconLifeBuoy,
    IconLink2,
    IconLink,
    IconLinkedin,
    IconList,
    IconLoader,
    IconLock,
    IconLogIn,
    IconLogOut,
    IconMail,
    IconMapPin,
    IconMap,
    IconMaximize2,
    IconMaximize,
    IconMeh,
    IconMenu,
    IconMessageCircle,
    IconMessageSquare,
    IconMicOff,
    IconMic,
    IconMinimize2,
    IconMinimize,
    IconMinusCircle,
    IconMinusSquare,
    IconMinus,
    IconMonitor,
    IconMoon,
    IconMoreHorizontal,
    IconMoreVertical,
    IconMousePointer,
    IconMove,
    IconMusic,
    IconNavigation2,
    IconNavigation,
    IconOctagon,
    IconPackage,
    IconPaperclip,
    IconPauseCircle,
    IconPause,
    IconPenTool,
    IconPercent,
    IconPhoneCall,
    IconPhoneForwarded,
    IconPhoneIncoming,
    IconPhoneMissed,
    IconPhoneOff,
    IconPhoneOutgoing,
    IconPhone,
    IconPieChart,
    IconPlayCircle,
    IconPlay,
    IconPlusCircle,
    IconPlusSquare,
    IconPlus,
    IconPocket,
    IconPower,
    IconPrinter,
    IconRadio,
    IconRefreshCcw,
    IconRefreshCw,
    IconRepeat,
    IconRewind,
    IconRotateCcw,
    IconRotateCw,
    IconRss,
    IconSave,
    IconScissors,
    IconSearch,
    IconSend,
    IconServer,
    IconSettings,
    IconShare2,
    IconShare,
    IconShieldOff,
    IconShield,
    IconShoppingBag,
    IconShoppingCart,
    IconShuffle,
    IconSidebar,
    IconSkipBack,
    IconSkipForward,
    IconSlack,
    IconSlash,
    IconSliders,
    IconSmartphone,
    IconSmile,
    IconSpeaker,
    IconSquare,
    IconStar,
    IconStopCircle,
    IconSun,
    IconSunrise,
    IconSunset,
    IconTable,
    IconTablet,
    IconTag,
    IconTarget,
    IconTerminal,
    IconThermometer,
    IconThumbsDown,
    IconThumbsUp,
    IconToggleLeft,
    IconToggleRight,
    IconTool,
    IconTrash2,
    IconTrash,
    IconTrello,
    IconTrendingDown,
    IconTrendingUp,
    IconTriangle,
    IconTruck,
    IconTv,
    IconTwitch,
    IconTwitter,
    IconType,
    IconUmbrella,
    IconUnderline,
    IconUnlock,
    IconUploadCloud,
    IconUpload,
    IconUserCheck,
    IconUserMinus,
    IconUserPlus,
    IconUserX,
    IconUser,
    IconUsers,
    IconVideoOff,
    IconVideo,
    IconVoicemail,
    IconVolume1,
    IconVolume2,
    IconVolumeX,
    IconVolume,
    IconWatch,
    IconWifiOff,
    IconWifi,
    IconWind,
    IconXCircle,
    IconXOctagon,
    IconXSquare,
    IconX,
    IconYoutube,
    IconZapOff,
    IconZap,
    IconZoomIn,
    IconZoomOut,
  },
  props: {
    size: {
      type: Number,
      default: 16,
      validator: function (value) {
        return [16,24].indexOf(value) !== -1;
      },
    },
    color: {
      type: String,
      default: "black",
      validator: function (c) {
        return ColorsArray.indexOf(c) !== -1;
      },
    },
    name: {
      type: String,
      required: true,
    },
  },
  computed: {
    colorhex() {
      return Colors[this.color];
    },
    classes() {
      return {
        "my-icon": true,
        [`my-icon--name-${this.name}`]: true,
        [`my-icon--size-${this.size}`]: true,
      };
    },
    style() {
      return {
        stroke: this.colorhex,
        width: this.size,
        height: this.size,
        "stroke-width": this.size == "16" ? 1 : 1.5,
      };
    },
    dynamicComponent() {
      switch (this.name) {
        case "activity":
          return IconActivity;
        case "airplay":
          return IconAirplay;
        case "alert-circle":
          return IconAlertCircle;
        case "alert-octagon":
          return IconAlertOctagon;
        case "alert-triangle":
          return IconAlertTriangle;
        case "align-center":
          return IconAlignCenter;
        case "align-justify":
          return IconAlignJustify;
        case "align-left":
          return IconAlignLeft;
        case "align-right":
          return IconAlignRight;
        case "anchor":
          return IconAnchor;
        case "aperture":
          return IconAperture;
        case "archive":
          return IconArchive;
        case "arrow-down-circle":
          return IconArrowDownCircle;
        case "arrow-down-left":
          return IconArrowDownLeft;
        case "arrow-down-right":
          return IconArrowDownRight;
        case "arrow-down":
          return IconArrowDown;
        case "arrow-left-circle":
          return IconArrowLeftCircle;
        case "arrow-left":
          return IconArrowLeft;
        case "arrow-right-circle":
          return IconArrowRightCircle;
        case "arrow-right":
          return IconArrowRight;
        case "arrow-up-circle":
          return IconArrowUpCircle;
        case "arrow-up-left":
          return IconArrowUpLeft;
        case "arrow-up-right":
          return IconArrowUpRight;
        case "arrow-up":
          return IconArrowUp;
        case "at-sign":
          return IconAtSign;
        case "award":
          return IconAward;
        case "bar-chart-2":
          return IconBarChart2;
        case "bar-chart":
          return IconBarChart;
        case "battery-charging":
          return IconBatteryCharging;
        case "battery":
          return IconBattery;
        case "bell-off":
          return IconBellOff;
        case "bell":
          return IconBell;
        case "bluetooth":
          return IconBluetooth;
        case "bold":
          return IconBold;
        case "book-open":
          return IconBookOpen;
        case "book":
          return IconBook;
        case "bookmark":
          return IconBookmark;
        case "box":
          return IconBox;
        case "briefcase":
          return IconBriefcase;
        case "calendar":
          return IconCalendar;
        case "camera-off":
          return IconCameraOff;
        case "camera":
          return IconCamera;
        case "cast":
          return IconCast;
        case "check-circle":
          return IconCheckCircle;
        case "check-square":
          return IconCheckSquare;
        case "check":
          return IconCheck;
        case "chevron-down":
          return IconChevronDown;
        case "chevron-left":
          return IconChevronLeft;
        case "chevron-right":
          return IconChevronRight;
        case "chevron-up":
          return IconChevronUp;
        case "chevrons-down":
          return IconChevronsDown;
        case "chevrons-left":
          return IconChevronsLeft;
        case "chevrons-right":
          return IconChevronsRight;
        case "chevrons-up":
          return IconChevronsUp;
        case "chrome":
          return IconChrome;
        case "circle":
          return IconCircle;
        case "clipboard":
          return IconClipboard;
        case "clock":
          return IconClock;
        case "cloud-drizzle":
          return IconCloudDrizzle;
        case "cloud-lightning":
          return IconCloudLightning;
        case "cloud-off":
          return IconCloudOff;
        case "cloud-rain":
          return IconCloudRain;
        case "cloud-snow":
          return IconCloudSnow;
        case "cloud":
          return IconCloud;
        case "code":
          return IconCode;
        case "codepen":
          return IconCodepen;
        case "codesandbox":
          return IconCodesandbox;
        case "coffee":
          return IconCoffee;
        case "columns":
          return IconColumns;
        case "command":
          return IconCommand;
        case "compass":
          return IconCompass;
        case "copy":
          return IconCopy;
        case "corner-down-left":
          return IconCornerDownLeft;
        case "corner-down-right":
          return IconCornerDownRight;
        case "corner-left-down":
          return IconCornerLeftDown;
        case "corner-left-up":
          return IconCornerLeftUp;
        case "corner-right-down":
          return IconCornerRightDown;
        case "corner-right-up":
          return IconCornerRightUp;
        case "corner-up-left":
          return IconCornerUpLeft;
        case "corner-up-right":
          return IconCornerUpRight;
        case "cpu":
          return IconCpu;
        case "credit-card":
          return IconCreditCard;
        case "crop":
          return IconCrop;
        case "crosshair":
          return IconCrosshair;
        case "database":
          return IconDatabase;
        case "delete":
          return IconDelete;
        case "disc":
          return IconDisc;
        case "divide-circle":
          return IconDivideCircle;
        case "divide-square":
          return IconDivideSquare;
        case "divide":
          return IconDivide;
        case "dollar-sign":
          return IconDollarSign;
        case "download-cloud":
          return IconDownloadCloud;
        case "download":
          return IconDownload;
        case "dribbble":
          return IconDribbble;
        case "droplet":
          return IconDroplet;
        case "edit-2":
          return IconEdit2;
        case "edit-3":
          return IconEdit3;
        case "edit":
          return IconEdit;
        case "external-link":
          return IconExternalLink;
        case "eye-off":
          return IconEyeOff;
        case "eye":
          return IconEye;
        case "facebook":
          return IconFacebook;
        case "fast-forward":
          return IconFastForward;
        case "feather":
          return IconFeather;
        case "figma":
          return IconFigma;
        case "file-minus":
          return IconFileMinus;
        case "file-plus":
          return IconFilePlus;
        case "file-text":
          return IconFileText;
        case "file":
          return IconFile;
        case "film":
          return IconFilm;
        case "filter":
          return IconFilter;
        case "flag":
          return IconFlag;
        case "folder-minus":
          return IconFolderMinus;
        case "folder-plus":
          return IconFolderPlus;
        case "folder":
          return IconFolder;
        case "framer":
          return IconFramer;
        case "frown":
          return IconFrown;
        case "gift":
          return IconGift;
        case "git-branch":
          return IconGitBranch;
        case "git-commit":
          return IconGitCommit;
        case "git-merge":
          return IconGitMerge;
        case "git-pull-request":
          return IconGitPullRequest;
        case "github":
          return IconGithub;
        case "gitlab":
          return IconGitlab;
        case "globe":
          return IconGlobe;
        case "grid":
          return IconGrid;
        case "hard-drive":
          return IconHardDrive;
        case "hash":
          return IconHash;
        case "headphones":
          return IconHeadphones;
        case "heart":
          return IconHeart;
        case "help-circle":
          return IconHelpCircle;
        case "hexagon":
          return IconHexagon;
        case "home":
          return IconHome;
        case "image":
          return IconImage;
        case "inbox":
          return IconInbox;
        case "info":
          return IconInfo;
        case "instagram":
          return IconInstagram;
        case "italic":
          return IconItalic;
        case "key":
          return IconKey;
        case "layers":
          return IconLayers;
        case "layout":
          return IconLayout;
        case "life-buoy":
          return IconLifeBuoy;
        case "link-2":
          return IconLink2;
        case "link":
          return IconLink;
        case "linkedin":
          return IconLinkedin;
        case "list":
          return IconList;
        case "loader":
          return IconLoader;
        case "lock":
          return IconLock;
        case "log-in":
          return IconLogIn;
        case "log-out":
          return IconLogOut;
        case "mail":
          return IconMail;
        case "map-pin":
          return IconMapPin;
        case "map":
          return IconMap;
        case "maximize-2":
          return IconMaximize2;
        case "maximize":
          return IconMaximize;
        case "meh":
          return IconMeh;
        case "menu":
          return IconMenu;
        case "message-circle":
          return IconMessageCircle;
        case "message-square":
          return IconMessageSquare;
        case "mic-off":
          return IconMicOff;
        case "mic":
          return IconMic;
        case "minimize-2":
          return IconMinimize2;
        case "minimize":
          return IconMinimize;
        case "minus-circle":
          return IconMinusCircle;
        case "minus-square":
          return IconMinusSquare;
        case "minus":
          return IconMinus;
        case "monitor":
          return IconMonitor;
        case "moon":
          return IconMoon;
        case "more-horizontal":
          return IconMoreHorizontal;
        case "more-vertical":
          return IconMoreVertical;
        case "mouse-pointer":
          return IconMousePointer;
        case "move":
          return IconMove;
        case "music":
          return IconMusic;
        case "navigation-2":
          return IconNavigation2;
        case "navigation":
          return IconNavigation;
        case "octagon":
          return IconOctagon;
        case "package":
          return IconPackage;
        case "paperclip":
          return IconPaperclip;
        case "pause-circle":
          return IconPauseCircle;
        case "pause":
          return IconPause;
        case "pen-tool":
          return IconPenTool;
        case "percent":
          return IconPercent;
        case "phone-call":
          return IconPhoneCall;
        case "phone-forwarded":
          return IconPhoneForwarded;
        case "phone-incoming":
          return IconPhoneIncoming;
        case "phone-missed":
          return IconPhoneMissed;
        case "phone-off":
          return IconPhoneOff;
        case "phone-outgoing":
          return IconPhoneOutgoing;
        case "phone":
          return IconPhone;
        case "pie-chart":
          return IconPieChart;
        case "play-circle":
          return IconPlayCircle;
        case "play":
          return IconPlay;
        case "plus-circle":
          return IconPlusCircle;
        case "plus-square":
          return IconPlusSquare;
        case "plus":
          return IconPlus;
        case "pocket":
          return IconPocket;
        case "power":
          return IconPower;
        case "printer":
          return IconPrinter;
        case "radio":
          return IconRadio;
        case "refresh-ccw":
          return IconRefreshCcw;
        case "refresh-cw":
          return IconRefreshCw;
        case "repeat":
          return IconRepeat;
        case "rewind":
          return IconRewind;
        case "rotate-ccw":
          return IconRotateCcw;
        case "rotate-cw":
          return IconRotateCw;
        case "rss":
          return IconRss;
        case "save":
          return IconSave;
        case "scissors":
          return IconScissors;
        case "search":
          return IconSearch;
        case "send":
          return IconSend;
        case "server":
          return IconServer;
        case "settings":
          return IconSettings;
        case "share-2":
          return IconShare2;
        case "share":
          return IconShare;
        case "shield-off":
          return IconShieldOff;
        case "shield":
          return IconShield;
        case "shopping-bag":
          return IconShoppingBag;
        case "shopping-cart":
          return IconShoppingCart;
        case "shuffle":
          return IconShuffle;
        case "sidebar":
          return IconSidebar;
        case "skip-back":
          return IconSkipBack;
        case "skip-forward":
          return IconSkipForward;
        case "slack":
          return IconSlack;
        case "slash":
          return IconSlash;
        case "sliders":
          return IconSliders;
        case "smartphone":
          return IconSmartphone;
        case "smile":
          return IconSmile;
        case "speaker":
          return IconSpeaker;
        case "square":
          return IconSquare;
        case "star":
          return IconStar;
        case "stop-circle":
          return IconStopCircle;
        case "sun":
          return IconSun;
        case "sunrise":
          return IconSunrise;
        case "sunset":
          return IconSunset;
        case "table":
          return IconTable;
        case "tablet":
          return IconTablet;
        case "tag":
          return IconTag;
        case "target":
          return IconTarget;
        case "terminal":
          return IconTerminal;
        case "thermometer":
          return IconThermometer;
        case "thumbs-down":
          return IconThumbsDown;
        case "thumbs-up":
          return IconThumbsUp;
        case "toggle-left":
          return IconToggleLeft;
        case "toggle-right":
          return IconToggleRight;
        case "tool":
          return IconTool;
        case "trash-2":
          return IconTrash2;
        case "trash":
          return IconTrash;
        case "trello":
          return IconTrello;
        case "trending-down":
          return IconTrendingDown;
        case "trending-up":
          return IconTrendingUp;
        case "triangle":
          return IconTriangle;
        case "truck":
          return IconTruck;
        case "tv":
          return IconTv;
        case "twitch":
          return IconTwitch;
        case "twitter":
          return IconTwitter;
        case "type":
          return IconType;
        case "umbrella":
          return IconUmbrella;
        case "underline":
          return IconUnderline;
        case "unlock":
          return IconUnlock;
        case "upload-cloud":
          return IconUploadCloud;
        case "upload":
          return IconUpload;
        case "user-check":
          return IconUserCheck;
        case "user-minus":
          return IconUserMinus;
        case "user-plus":
          return IconUserPlus;
        case "user-x":
          return IconUserX;
        case "user":
          return IconUser;
        case "users":
          return IconUsers;
        case "video-off":
          return IconVideoOff;
        case "video":
          return IconVideo;
        case "voicemail":
          return IconVoicemail;
        case "volume-1":
          return IconVolume1;
        case "volume-2":
          return IconVolume2;
        case "volume-x":
          return IconVolumeX;
        case "volume":
          return IconVolume;
        case "watch":
          return IconWatch;
        case "wifi-off":
          return IconWifiOff;
        case "wifi":
          return IconWifi;
        case "wind":
          return IconWind;
        case "x-circle":
          return IconXCircle;
        case "x-octagon":
          return IconXOctagon;
        case "x-square":
          return IconXSquare;
        case "x":
          return IconX;
        case "youtube":
          return IconYoutube;
        case "zap-off":
          return IconZapOff;
        case "zap":
          return IconZap;
        case "zoom-in":
          return IconZoomIn;
        case "zoom-out":
          return IconZoomOut;
        default:
          return `Icon ${this.name} not found`;
      }
    },
  }
};

</script>