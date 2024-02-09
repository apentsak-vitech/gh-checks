<span style="color:red">-</span>/<span style="color:green">+</span> resource "aws_s3_bucket" "this"{
   <span style="color:green">+</span>acceleration_status         = (known after apply)
   <span style="color:green">+</span>acl                         = (known after apply)
    <span style="color:yellow">~</span> arn                         = "arn:aws:s3:::asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    <span style="color:yellow">~</span> bucket                      = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv" # forces replacement
    <span style="color:yellow">~</span> bucket_domain_name          = "asd23ffdf--dsfvd--fdr4grefdv.s3.amazonaws.com" -> (known after apply)
   <span style="color:green">+</span>bucket_prefix               = (known after apply)
    <span style="color:yellow">~</span> bucket_regional_domain_name = "asd23ffdf--dsfvd--fdr4grefdv.s3.us-east-1.amazonaws.com" -> (known after apply)
    <span style="color:yellow">~</span> hosted_zone_id              = "ASDASDASD2342342" -> (known after apply)
    <span style="color:yellow">~</span> id                          = "asd23ffdf--dsfvd--fdr4grefdv" -> (known after apply)
    <span style="color:yellow">~</span> object_lock_enabled         = false -> (known after apply)
   <span style="color:green">+</span>policy                      = (known after apply)
    <span style="color:yellow">~</span> region                      = "us-east-1" -> (known after apply)
    <span style="color:yellow">~</span> request_payer               = "BucketOwner" -> (known after apply)
    <span style="color:yellow">~</span> tags                        = {
        <span style="color:yellow">~</span> "Name" = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
       <span style="color:green">+</span>"demo" = "demo"
      }
    <span style="color:yellow">~</span> tags_all                    = {
        <span style="color:yellow">~</span> "Name"              = "asd23ffdf--dsfvd--fdr4grefdv" -> "asd23ffdf--dsfvd4-fdr4grefdv"
       <span style="color:green">+</span>"demo"              = "demo"
          # (6 unchanged elements hidden)
      }
   <span style="color:green">+</span>website_domain              = (known after apply)
   <span style="color:green">+</span>website_endpoint            = (known after apply)
      # (1 unchanged attribute hidden)

   <span style="color:red">-</span>grant {
       <span style="color:red">-</span>id          = "80730b374aa1bb2deb9cc2a53aab494b20b2deacd106cd5e5e4fe7cbf56a1d85" -> null
       <span style="color:red">-</span>permissions = [
           <span style="color:red">-</span>"FULL_CONTROL",
          ] -> null
       <span style="color:red">-</span>type        = "CanonicalUser" -> null
      }

   <span style="color:red">-</span>server_side_encryption_configuration {
       <span style="color:red">-</span>rule {
           <span style="color:red">-</span>bucket_key_enabled = false -> null

           <span style="color:red">-</span>apply_server_side_encryption_by_default {
               <span style="color:red">-</span>sse_algorithm = "AES256" -> null
              }
          }
      }

   <span style="color:red">-</span>versioning {
       <span style="color:red">-</span>enabled    = false -> null
       <span style="color:red">-</span>mfa_delete = false -> null
      }
  }

# aws_s3_object.this must be replaced
<span style="color:red">-</span>/<span style="color:green">+</span> resource "aws_s3_object" "this" {
   <span style="color:green">+</span>acl                    = (known after apply)
    <span style="color:yellow">~</span> bucket                 = "asd23ffdf--dsfvd--fdr4grefdv" # forces replacement -> (known after apply) # forces replacement
    <span style="color:yellow">~</span> bucket_key_enabled     = false -> (known after apply)
   <span style="color:green">+</span>checksum_crc32         = (known after apply)
   <span style="color:green">+</span>checksum_crc32c        = (known after apply)
   <span style="color:green">+</span>checksum_sha1          = (known after apply)
   <span style="color:green">+</span>checksum_sha256        = (known after apply)
    <span style="color:yellow">~</span> content_type           = "application/octet-stream" -> (known after apply)
    <span style="color:yellow">~</span> id                     = "data.txt" -> (known after apply)
   <span style="color:green">+</span>kms_key_id             = (known after apply)
   <span style="color:red">-</span>metadata               = {} -> null
    <span style="color:yellow">~</span> server_side_encryption = "AES256" -> (known after apply)
    <span style="color:yellow">~</span> storage_class          = "STANDARD" -> (known after apply)
   <span style="color:red">-</span>tags                   = {} -> null
   <span style="color:green">+</span>version_id             = (known after apply)
      # (4 unchanged attributes hidden)
  }

Plan: 2 to add, 0 to change, 2 to destroy.

─────────────────────────────────────────────────────────────────────────────

Saved the plan to:
/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan

To perform exactly these actions, run the following command to apply:
  terraform apply "/home/runner/iac-tf_terragrunt_aaws_asd23ffdf_s3.tfplan"