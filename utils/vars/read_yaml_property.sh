rp() {
  local property_path="$1"
  local default_value="$2"
  local file_path="$3"

  # If the third argument is not provided, use DEVX_CONF if available
  if [ -z "$file_path" ]; then
    if [ -n "$DEVX_CONF" ]; then
      file_path="$DEVX_CONF"
    else
      echo "Error: Missing file path and DEVX_CONF environment variable is not set."
      return 1
    fi
  fi

  # Check if the file exists
  if [ ! -f "$file_path" ]; then
    echo "Error: The specified file '$file_path' does not exist."
    return 1
  fi

  # Use yq to extract the property value
  local property_value
  property_value=$(yq eval "$property_path" "$file_path")

  if [ "$property_value" = "null" ] || [ -z "$property_value" ]; then
    if [ -n "$default_value" ]; then
      echo "$default_value"
    else
      echo "Error: Property '$property_path' not found in '$file_path'."
      return 1
    fi
  else
    echo "$property_value"
  fi
}


