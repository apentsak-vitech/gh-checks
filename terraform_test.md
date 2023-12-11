random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"


random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"


random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"


random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

random_string.this: Refreshing state... [id=z9jkzzu8i7iiiq0z]
aws_s3_bucket.this: Refreshing state... [id=qa--cat3--z9jkzzu8i7iiiq0z]
aws_s3_object.this: Refreshing state... [id=data.txt]

-/+ resource "aws_s3_bucket" "this" {
    + acceleration_status         = (known after apply)
    + acl                         = (known after apply)
    ~ arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    ~ bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
    + bucket_prefix               = (known after apply)
    ~ bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    ~ hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    ~ id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    ~ object_lock_enabled         = false -> (known after apply)
    + policy                      = (known after apply)
    ~ region                      = "us-east-1" -> (known after apply)
    ~ request_payer               = "BucketOwner" -> (known after apply)
    ~ tags                        = {
        ~ "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo" = "demo"
      }
    ~ tags_all                    = {
        ~ "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
        + "demo"              = "demo"
          # (6 unchanged elements hidden)
      }
    + website_domain              = (known after apply)
    + website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

    - grant {
        - id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
        - permissions = [
            - "FULL_CONTROL",
          ] -> null
        - type        = "CanonicalUser" -> null
      }

    - server_side_encryption_configuration {
        - rule {
            - bucket_key_enabled = false -> null

            - apply_server_side_encryption_by_default {
                - sse_algorithm = "AES256" -> null
              }
          }
      }

    - versioning {
        - enabled    = false -> null
        - mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
-/+ resource "aws_s3_object" "this" {
    + acl                    = (known after apply)
    ~ bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    ~ bucket_key_enabled     = false -> (known after apply)
    + checksum_crc32         = (known after apply)
    + checksum_crc32c        = (known after apply)
    + checksum_sha1          = (known after apply)
    + checksum_sha256        = (known after apply)
    ~ content_type           = "application/octet-stream" -> (known after apply)
    ~ id                     = "data.txt" -> (known after apply)
    + kms_key_id             = (known after apply)
    - metadata               = {} -> null
    ~ server_side_encryption = "AES256" -> (known after apply)
    ~ storage_class          = "STANDARD" -> (known after apply)
    - tags                   = {} -> null
    + version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"