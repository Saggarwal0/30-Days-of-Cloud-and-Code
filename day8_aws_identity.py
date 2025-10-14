#!/usr/bin/env python3
"""
Day 8 — AWS STS Identity Check (Account / ARN / UserId)

Usage:
  python day8_aws_identity.py
  python day8_aws_identity.py --profile myprofile
  python day8_aws_identity.py --role-arn arn:aws:iam::123456789012:role/Dev --session-name test
  python day8_aws_identity.py --json
"""

import argparse
import json
import sys
import boto3
from botocore.exceptions import BotoCoreError, ClientError

def make_sts(profile: str | None):
    if profile:
        session = boto3.Session(profile_name=profile)
    else:
        session = boto3.Session()
    return session.client("sts"), session.region_name or "us-east-1"

def assume_role(base_sts, role_arn: str, session_name: str, duration: int = 3600):
    resp = base_sts.assume_role(
        RoleArn=role_arn,
        RoleSessionName=session_name,
        DurationSeconds=duration
    )
    c = resp["Credentials"]
    session = boto3.Session(
        aws_access_key_id=c["AccessKeyId"],
        aws_secret_access_key=c["SecretAccessKey"],
        aws_session_token=c["SessionToken"],
    )
    return session.client("sts")

def main():
    p = argparse.ArgumentParser(description="AWS STS identity check")
    p.add_argument("--profile", help="AWS named profile (from ~/.aws/config)")
    p.add_argument("--role-arn", help="Assume this role first")
    p.add_argument("--session-name", default="day8-identity-check", help="Role session name")
    p.add_argument("--json", action="store_true", help="Print raw JSON")
    args = p.parse_args()

    try:
        sts, region = make_sts(args.profile)
        if args.role_arn:
            sts = assume_role(sts, args.role_arn, args.session_name)

        ident = sts.get_caller_identity()  # {'Account','Arn','UserId'}

        if args.json:
            print(json.dumps({"Region": region, **ident}, indent=2))
            return

        print("✅ AWS STS Identity")
        print(f"  Account : {ident.get('Account')}")
        print(f"  ARN     : {ident.get('Arn')}")
        print(f"  UserId  : {ident.get('UserId')}")
        print(f"  Region  : {region}")
    except (BotoCoreError, ClientError) as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
