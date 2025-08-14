// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from darknet_ros_msgs:msg/BoundingBox.idl
// generated code does not contain a copyright notice

#include "darknet_ros_msgs/msg/detail/bounding_box__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_darknet_ros_msgs
const rosidl_type_hash_t *
darknet_ros_msgs__msg__BoundingBox__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x3b, 0xcb, 0x50, 0x8b, 0xd9, 0x5f, 0xae, 0x98,
      0xb3, 0x58, 0x50, 0x86, 0x27, 0x2a, 0xc0, 0x1a,
      0xbf, 0xde, 0xcc, 0x1b, 0x84, 0x2a, 0x66, 0x00,
      0x31, 0xc8, 0xb7, 0x96, 0x62, 0x5d, 0xe9, 0xe9,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char darknet_ros_msgs__msg__BoundingBox__TYPE_NAME[] = "darknet_ros_msgs/msg/BoundingBox";

// Define type names, field names, and default values
static char darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__probability[] = "probability";
static char darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__xmin[] = "xmin";
static char darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__ymin[] = "ymin";
static char darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__xmax[] = "xmax";
static char darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__ymax[] = "ymax";
static char darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__id[] = "id";
static char darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__class_id[] = "class_id";

static rosidl_runtime_c__type_description__Field darknet_ros_msgs__msg__BoundingBox__FIELDS[] = {
  {
    {darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__probability, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__xmin, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT64,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__ymin, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT64,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__xmax, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT64,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__ymax, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT64,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__id, 2, 2},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_INT16,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {darknet_ros_msgs__msg__BoundingBox__FIELD_NAME__class_id, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
darknet_ros_msgs__msg__BoundingBox__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {darknet_ros_msgs__msg__BoundingBox__TYPE_NAME, 32, 32},
      {darknet_ros_msgs__msg__BoundingBox__FIELDS, 7, 7},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "float64 probability\n"
  "int64 xmin\n"
  "int64 ymin\n"
  "int64 xmax\n"
  "int64 ymax\n"
  "int16 id\n"
  "string class_id";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
darknet_ros_msgs__msg__BoundingBox__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {darknet_ros_msgs__msg__BoundingBox__TYPE_NAME, 32, 32},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 89, 89},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
darknet_ros_msgs__msg__BoundingBox__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *darknet_ros_msgs__msg__BoundingBox__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
