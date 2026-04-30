"""
Generate 150 completely new AI-quality phishing emails as a held-out test set.
These are distinct from the 200 emails in ai_safe_variants.csv.
Saved to: data/generated/ai_phishing_holdout_150.csv
"""
import csv
import pandas as pd
from pathlib import Path

# =============================================================================
# CATEGORY 1 — BANKING / FINANCIAL (20 emails)
# New banks and scenarios not covered in the original 200
# =============================================================================
BANKING_NEW = [

    """Subject: TD Bank: Your Online Account Has Been Temporarily Suspended

Dear TD Bank Customer,

We have detected multiple failed sign-in attempts on your TD Bank Online Banking account. As a precautionary security measure, your account has been temporarily suspended.

To restore access and confirm your identity, please complete the verification process through our secure portal:
https://tdbank-secure-verification.com/restore

You will need your account number, Social Security Number, and answers to your security questions. If you do not complete verification within 48 hours, your account will be permanently closed.

TD Bank Security Operations Center""",

    """Subject: American Express: Unusual Transaction Detected on Your Card

Dear Cardmember,

A transaction of $1,247.00 was attempted on your American Express card at an international merchant. Our fraud detection system has flagged this transaction as potentially unauthorized.

To dispute this charge and protect your account:
https://americanexpress-fraud-dispute.com/review

If you do not respond within 24 hours, the transaction will be processed and funds released to the merchant. American Express Fraud Protection covers eligible unauthorized charges.

American Express Fraud Prevention""",

    """Subject: Citizens Bank: Your Wire Transfer Has Been Placed on Hold

Dear Customer,

A wire transfer of $4,500.00 from your Citizens Bank checking account was flagged by our compliance team for additional verification. This transfer has been placed on hold pending your confirmation.

To authorize or cancel this transfer:
https://citizens-bank-wire-verify.com/confirm-transfer

Please verify this transaction within 12 hours, or the transfer will be automatically cancelled and a hold placed on your account pending review.

Citizens Bank Wire Transfer Security""",

    """Subject: USAA: Military Account Security Alert — Immediate Action Required

Dear USAA Member,

Your USAA account has been flagged for suspicious activity originating from a non-military IP address. As part of our commitment to protecting our military members, we have temporarily restricted your account access.

Please verify your identity and service record through our secure member portal:
https://usaa-member-verify.com/military-id

Your bank accounts, insurance policies, and investment accounts remain secure. Access will be restored upon successful verification.

USAA Fraud Prevention — Serving Those Who Served""",

    """Subject: Ally Bank: Your Online Savings Account Requires Verification

Dear Ally Customer,

Ally Bank is updating its identity verification systems in compliance with new federal banking regulations. All customers must re-verify their identity by the end of this month.

Customers who do not complete verification will have their accounts restricted from withdrawals and transfers until verification is complete.

Verify your identity here: https://ally-bank-id-verify.com/update

This process requires your government-issued ID and a recent utility bill or bank statement.

Ally Bank Compliance Department""",

    """Subject: Navy Federal Credit Union: Account Access Has Been Restricted

Dear Member,

Your Navy Federal Credit Union account access has been restricted due to a failed address verification on your latest statement. Federal regulations require us to maintain accurate member records.

To update your information and restore full account access:
https://navyfederal-member-update.com/address-verify

Members of our armed forces, veterans, and their families deserve the best protection. Please complete this update within 72 hours.

Navy Federal Credit Union Member Services""",

    """Subject: Discover Bank: Your Cashback Bonus Balance Is About to Expire

Dear Discover Customer,

Our records show you have $342.00 in unredeemed Cashback Bonus that is scheduled to expire at the end of this billing cycle. Unclaimed cashback cannot be recovered after the expiration date.

Redeem your cashback balance now:
https://discover-cashback-redeem.com/claim-bonus

You may apply your cashback as a statement credit, direct deposit, or gift card. Log in to your Discover account to complete your redemption.

Discover Rewards Center""",

    """Subject: PNC Bank: Your Account Will Be Closed Due to Inactivity

Dear PNC Customer,

Our records show that your PNC checking account has been inactive for more than 12 months. Under our Account Maintenance Policy, inactive accounts are subject to closure after 90 days of notice.

To reactivate your account and prevent closure:
https://pnc-account-reactivate.com/verify-identity

Reactivation requires identity verification and a qualifying transaction within 30 days. Any remaining balance will be mailed to your address on file if the account is closed.

PNC Bank Account Services""",

    """Subject: Regions Bank: Your Debit Card Has Been Reported Lost or Stolen

Dear Regions Customer,

Our fraud monitoring system has been notified that your Regions Bank debit card ending in 4821 may have been compromised. As a precautionary measure, we have disabled the card and are issuing a replacement.

To expedite your replacement card and unlock your account:
https://regions-bank-card-replace.com/verify

Standard replacement takes 7–10 business days. To receive your card within 2 business days, select the expedited delivery option and confirm your shipping address.

Regions Bank Card Services""",

    """Subject: HSBC: International Wire Transfer — Verification Required

Dear HSBC Customer,

An international wire transfer of USD $8,200.00 has been initiated from your HSBC account to a recipient in Singapore. This transfer requires additional verification under our international compliance policy.

To approve or cancel this transfer:
https://hsbc-international-wire.com/verify-transfer

HSBC is required by law to verify international transfers exceeding $5,000. Failure to verify within 6 hours will result in automatic cancellation and a temporary account freeze.

HSBC Global Compliance""",

    """Subject: KeyBank: Your Mortgage Payment Failed — Action Required

Dear KeyBank Customer,

Your scheduled mortgage payment of $2,143.00 due on the 1st of this month was returned by your bank due to insufficient funds. Your mortgage account is now 5 days past due.

To make a payment and avoid late fees or credit reporting:
https://keybank-mortgage-payment.com/make-payment

A late fee of $75.00 will be assessed if payment is not received within 15 days. Payments 30+ days late will be reported to the credit bureaus.

KeyBank Mortgage Services""",

    """Subject: Citibank: Foreign Transaction Alert — Unauthorized Use Detected

Dear Citi Customer,

Your Citibank account was used for a purchase of €892.00 at a merchant in Germany. Our system has flagged this as potentially unauthorized based on your recent account activity and location.

To dispute this transaction immediately:
https://citi-foreign-transaction-dispute.com/review

If you do not respond within 24 hours, our ability to reverse this charge may be limited. We recommend also updating your PIN and online banking password.

Citibank Fraud Protection Services""",

    """Subject: Fifth Third Bank: Direct Deposit Failed — Payroll Issue

Dear Account Holder,

Your most recent direct deposit of $3,287.00 from your employer was rejected by Fifth Third Bank due to a routing number mismatch in our system. The funds have been returned to your employer's payroll processor.

To correct your routing information and receive your pay:
https://53bank-deposit-correction.com/update-routing

Please update your banking information with your employer's HR or payroll department as well. This issue affects your current and future direct deposits.

Fifth Third Bank Payment Services""",

    """Subject: SunTrust (Now Truist): Your Account Migration Is Incomplete

Dear Customer,

As part of the SunTrust and BB&T merger into Truist Bank, your account migration was not completed successfully. Your SunTrust account credentials are no longer valid, and you must complete your Truist account setup.

Complete your account migration:
https://truist-migration-complete.com/setup-account

During this transition, some features may be temporarily unavailable. Please complete your migration by the end of this month to avoid service interruption.

Truist Bank Account Migration Team""",

    """Subject: Huntington Bank: Overdraft Protection — Immediate Payment Required

Dear Huntington Customer,

Your Huntington Bank checking account has overdrawn by $478.32. Under our Overdraft Protection policy, you have 24 hours to bring your account to a positive balance before fees are assessed.

Make a deposit or transfer now:
https://huntington-overdraft-payment.com/deposit

A $36.00 overdraft fee will be charged for each business day your account remains negative. Additionally, your debit card transactions may be declined until the balance is restored.

Huntington National Bank""",

    """Subject: Zelle: You Have a Pending Payment Requiring Verification

Dear Zelle User,

A payment of $750.00 has been sent to you via Zelle but is currently pending verification. To release this payment to your bank account, you must verify your Zelle account.

Verify and claim your payment:
https://zelle-payment-verify.com/claim-funds

Your Zelle account must be verified within 48 hours or the payment will be returned to the sender. Zelle payments are instant once verification is complete.

Zelle Payment Network""",

    """Subject: Fidelity Investments: Your Brokerage Account Has Been Temporarily Locked

Dear Fidelity Customer,

We have detected login attempts from an unrecognized device and location on your Fidelity brokerage account. To protect your investments, we have temporarily locked your account.

Restore access to your account:
https://fidelity-account-restore.com/identity-verify

During the lock period, you will not be able to place trades, transfer funds, or access your portfolio. Please complete identity verification within 24 hours.

Fidelity Investments Security Operations""",

    """Subject: Charles Schwab: Mandatory Account Re-Verification Required

Dear Schwab Client,

As part of our enhanced Know Your Customer (KYC) compliance program, all Schwab account holders are required to re-verify their identity and update their account information.

Accounts not verified by the deadline will have trading and transfer privileges suspended until verification is complete.

Complete your verification: https://schwab-kyc-verify.com/update-information

This process requires a government-issued photo ID and proof of current address (utility bill or bank statement dated within 90 days).

Charles Schwab Compliance Department""",

    """Subject: Robinhood: Your Account Has Been Restricted — Verify Identity

Dear Robinhood User,

Your Robinhood account has been restricted following a review of recent trading activity. To restore your account and continue trading stocks, ETFs, and options, you must verify your identity.

Verify your account now: https://robinhood-identity-verify.com/restore-access

During the restriction period, you may not place new orders or withdraw funds. Your existing positions are unaffected.

Robinhood Financial Compliance Team""",

    """Subject: Vanguard: Rollover IRA Verification Required — Deadline Tomorrow

Dear Vanguard Investor,

Your IRA rollover request of $42,500.00 is on hold pending identity verification. Federal regulations require additional verification for rollovers exceeding $10,000.

To complete your rollover and avoid tax withholding:
https://vanguard-ira-rollover.com/verify-identity

If verification is not completed within 24 hours, we will be required to withhold 20% of the rollover amount for federal taxes and return the remainder to you.

Vanguard Retirement Services""",

]

# =============================================================================
# CATEGORY 2 — IT / TECH ALERTS (15 emails)
# New platforms and scenarios
# =============================================================================
IT_NEW = [

    """Subject: Adobe Creative Cloud: Your Subscription Has Been Cancelled

Dear Adobe Customer,

Your Adobe Creative Cloud subscription has been cancelled due to a failed payment. Access to all Adobe applications — including Photoshop, Illustrator, Premiere Pro, and Acrobat — will be terminated in 24 hours.

To restore your subscription and retain your files:
https://adobe-creative-cloud-restore.com/reactivate

Upon successful payment, your subscription will be restored immediately with no interruption to your projects or cloud storage.

Adobe Customer Care""",

    """Subject: AWS: Your Account Has Been Suspended Due to Policy Violation

Dear AWS Customer,

Your Amazon Web Services account has been suspended following the detection of activity that violates the AWS Acceptable Use Policy. All running instances, databases, and services have been terminated.

To appeal this suspension and restore your account:
https://aws-account-appeal.com/submit-review

If this suspension is not appealed within 7 days, all data and resources associated with your account will be permanently deleted. Your billing will be paused during the suspension period.

Amazon Web Services Trust & Safety""",

    """Subject: Meta Business Suite: Your Ad Account Has Been Disabled

Dear Advertiser,

Your Meta Business ad account has been disabled due to a violation of our Advertising Policies. All active campaigns, ad sets, and ads associated with your account have been paused.

To appeal this decision and restore your account:
https://meta-ads-appeal.com/submit-review

If your account is not restored within 30 days, all campaign data, audience lists, and creative assets will be permanently deleted.

Meta Ads Policy Team""",

    """Subject: Shopify: Your Store Has Been Temporarily Suspended

Dear Shopify Merchant,

Your Shopify store has been temporarily suspended due to a high rate of disputed charges (chargebacks) from customers. This suspension affects your storefront, checkout, and payment processing.

To resolve this issue and reopen your store:
https://shopify-store-restore.com/chargeback-review

You will need to provide documentation addressing the disputed charges. Stores suspended for more than 14 days may face permanent termination.

Shopify Risk and Compliance""",

    """Subject: GoDaddy: Your Domain Is Expiring in 24 Hours — Act Now

Dear Domain Owner,

Your domain registered with GoDaddy is scheduled to expire within 24 hours. If your domain expires, your website will go offline and your email addresses will stop working.

Renew your domain now to avoid interruption:
https://godaddy-domain-renew-now.com/renew

After expiration, there is a 30-day redemption period during which you may reclaim your domain for a $80 redemption fee. After 30 days, the domain is released to the public.

GoDaddy Domain Services""",

    """Subject: Norton: Your Device Is at Risk — Subscription Has Lapsed

Dear Norton Customer,

Your Norton 360 subscription expired 3 days ago. Your device is now unprotected against viruses, ransomware, spyware, and identity theft.

Reactivate your protection immediately:
https://norton-subscription-renew.com/reactivate

As a valued customer, we are offering a 60% discount on renewal if you act within the next 2 hours. Your existing Norton settings and preferences will be preserved.

Norton LifeLock Security""",

    """Subject: LastPass: Security Breach — Your Vault May Be Compromised

Dear LastPass User,

LastPass has detected that your master password may have been exposed in a recent data incident. We strongly recommend you change your master password and enable two-factor authentication immediately.

Secure your account now: https://lastpass-secure-account.com/reset-master

To protect your stored passwords, we recommend you also change the passwords for your most sensitive accounts (banking, email, social media) as a precautionary measure.

LastPass Security Team""",

    """Subject: Cloudflare: Your Domain SSL Certificate Has Expired

Dear Cloudflare Customer,

The SSL/TLS certificate for your domain managed through Cloudflare has expired. Visitors to your website are now seeing security warnings, which may cause significant loss of traffic and trust.

Renew your SSL certificate: https://cloudflare-ssl-renew.com/update-certificate

If you are using Cloudflare's Universal SSL, your certificate should renew automatically. If you are using a custom certificate, you must upload a new certificate before the certificate authority invalidates it.

Cloudflare Network Operations""",

    """Subject: Atlassian: Your Jira and Confluence Access Will Be Removed

Dear Atlassian User,

Your organization's Atlassian account administrator has initiated a license audit. Users who do not re-verify their account by end of day will have their Jira and Confluence access revoked.

Verify your Atlassian account: https://atlassian-account-verify.com/re-verify

This process takes less than 2 minutes. You will need to confirm your email address and re-authenticate with your organization credentials.

Atlassian Account Management""",

    """Subject: Twitter / X: Your Account Is Scheduled for Permanent Suspension

Dear X User,

Your X (formerly Twitter) account has received multiple reports for policy violations. After review, our Trust & Safety team has determined that your account will be permanently suspended in 48 hours unless you appeal.

Submit your appeal here: https://x-twitter-appeal.com/dispute-suspension

If your appeal is not submitted within the deadline, your account, all posts, followers, and direct messages will be permanently deleted and cannot be recovered.

X Trust & Safety""",

    """Subject: Webex: Your Cisco Webex License Has Expired — Meetings Disabled

Dear Webex User,

Your Cisco Webex Meetings license has expired. You are no longer able to host meetings with more than 2 participants. All scheduled meetings have been cancelled and participants notified.

Renew your Webex license: https://webex-license-renew.com/reactivate

As an existing customer, you qualify for a 40% discount on annual renewal. Contact your Cisco account representative or renew online before your grace period ends.

Cisco Webex Account Services""",

    """Subject: Notion: Your Workspace Billing Has Failed — Downgrade Imminent

Dear Notion User,

The payment method on file for your Notion Plus workspace has declined. If payment is not updated within 48 hours, your workspace will be downgraded to the free plan.

Downgrading will result in:
• Loss of unlimited blocks for all members
• Removal of version history beyond 7 days
• Removal of guest access for external collaborators

Update your payment method: https://notion-billing-update.com/payment

Notion Billing""",

    """Subject: Salesforce: Your CRM Instance Is Being Decommissioned

Dear Salesforce Administrator,

Your Salesforce CRM instance is scheduled for decommission due to an expired contract and outstanding balance of $4,872.00. All customer data, workflows, and integrations will be deleted in 7 days.

To resolve the billing issue and prevent data loss:
https://salesforce-account-resolve.com/billing

Salesforce offers a 30-day data export window after decommission. To initiate a data export or resume your subscription, contact us immediately.

Salesforce Account Management""",

    """Subject: McAfee: Your Subscription Is Expiring — 3 Devices at Risk

Dear McAfee Customer,

Your McAfee Total Protection subscription expires in 48 hours. Once expired, virus and malware protection will cease on all 3 of your registered devices.

Renew now at a 70% discount: https://mcafee-renew-subscription.com/special-offer

Cybercriminals frequently target unprotected devices within hours of subscription lapse. Don't leave your financial data, photos, and personal files unprotected.

McAfee Customer Protection Services""",

    """Subject: Dropbox Business: Your Team Account Will Be Deleted

Dear Dropbox Business Administrator,

Your Dropbox Business account has an unpaid balance of $287.00. Your account will be downgraded to a free personal plan in 72 hours, and all team members will lose access to shared folders and files.

To resolve this and restore team access:
https://dropbox-business-billing.com/pay-balance

Files stored in shared team folders will be moved to the account owner's personal folder. Files owned by team members will be inaccessible until the account is restored.

Dropbox Business Billing""",

]

# =============================================================================
# CATEGORY 3 — DELIVERY / SHIPPING (15 emails)
# New carriers and scenarios
# =============================================================================
DELIVERY_NEW = [

    """Subject: DHL Express: Your International Shipment Is Held at Customs

Dear Recipient,

Your DHL Express international shipment (Waybill: 1234567890) originating from London, UK has been held at U.S. Customs for inspection. A customs duty of $23.50 must be paid before your package can be released for delivery.

Pay customs duty and release your shipment:
https://dhl-customs-payment.com/pay-duty

Your shipment contains: Personal goods / Clothing. If payment is not received within 72 hours, the shipment will be returned to the sender at your expense.

DHL Express Customs Services""",

    """Subject: UPS: Signature Required — We Missed You Today

Dear UPS Customer,

Our driver attempted to deliver a package requiring your signature today at your registered address. A delivery notice was left at your door.

To reschedule delivery or authorize a release without signature:
https://ups-delivery-reschedule.com/schedule

Package details:
Tracking #: 1Z999AA10123456784
Estimated Value: $189.00
Sender: Undisclosed

A second delivery attempt will be made tomorrow. After 3 failed attempts, the package will be returned to the sender.

UPS Delivery Services""",

    """Subject: Amazon: Your Package Was Delivered to the Wrong Address

Dear Customer,

We have been notified that your recent Amazon delivery was accidentally delivered to an incorrect address. Our logistics team is currently attempting to retrieve your package.

To file a delivery claim and receive a replacement or refund:
https://amazon-delivery-claim.com/wrong-address

Your order details:
Order #: 114-5592847-2038472
Item: Electronics / Personal Care
Estimated Value: $89.97

Amazon stands behind every delivery. If we are unable to retrieve your package, a full refund or free replacement will be issued.

Amazon Logistics Customer Support""",

    """Subject: USPS: Your Certified Mail Requires a Digital Signature

Dear Recipient,

A Certified Mail item addressed to you could not be delivered because no one was available to sign. The item is now available for pickup at your local Post Office.

To avoid a trip to the Post Office, you may authorize delivery online:
https://usps-certified-mail-authorize.com/sign-online

Item details:
Tracking #: 9407111899223457394922
Sender: Government Agency / Legal Document
Hold Expires: In 3 business days

If the item is not picked up or delivery is not authorized within 15 days, it will be returned to the sender.

USPS Delivery Management""",

    """Subject: FedEx: Your Package Requires Address Correction — Delivery Delayed

Dear FedEx Customer,

Your incoming FedEx package (Tracking #: 774899172937) has been delayed because the delivery address on file is incomplete or incorrect. Our drivers were unable to locate the delivery point.

To provide the correct address and resume delivery:
https://fedex-address-correction.com/update

Your package is currently held at a FedEx facility near your original delivery address. If the correct address is not provided within 5 business days, the package will be returned to the shipper at your expense.

FedEx Customer Solutions""",

    """Subject: OnTrac: Delivery Exception — Package Held at Facility

Dear Customer,

Your OnTrac shipment (Tracking #: C10999800500862) has encountered a delivery exception and is being held at our distribution facility. A delivery attempt was made but the address was inaccessible.

To schedule a pickup or redelivery:
https://ontrac-delivery-reschedule.com/schedule-delivery

Your shipment will be held for 5 business days before being returned to the sender. Pickup is available during facility hours, Monday through Saturday.

OnTrac Customer Service""",

    """Subject: eBay: Your Purchased Item Has Not Been Shipped — Dispute Open

Dear eBay Buyer,

Your purchased item (Order #: 15-09482-71920) has not been shipped within the seller's stated handling time. A dispute has been automatically opened on your behalf.

To track your dispute status or escalate to eBay:
https://ebay-buyer-dispute.com/track-case

If the seller does not respond within 3 business days, eBay will issue a full refund to your original payment method under the eBay Money Back Guarantee.

eBay Buyer Protection""",

    """Subject: Instacart: Your Grocery Order Has a Missing Item — Refund Pending

Dear Instacart Customer,

Your Instacart grocery order (#IC-48291053) is missing 3 items that were out of stock at the time of shopping. A partial refund of $18.47 has been initiated to your payment method.

To confirm your refund or request a credit:
https://instacart-refund-confirm.com/order-review

Refunds typically appear within 5–10 business days depending on your bank. You may also choose Instacart credit, which is applied instantly to your account.

Instacart Customer Happiness Team""",

    """Subject: Shipt: Delivery Issue — Driver Needs Confirmation for Drop-Off

Dear Shipt Member,

Your Shipt driver is attempting to complete your delivery but needs to confirm your drop-off instructions. Without confirmation, your order cannot be left unattended.

Confirm your delivery preferences:
https://shipt-delivery-confirm.com/drop-off-instructions

Your order includes:
3 grocery bags — Total: $134.22

Please respond within 30 minutes or your order may be returned to the store and a cancellation fee applied.

Shipt Delivery Support""",

    """Subject: Pitney Bowes: Your Postage Meter Subscription Has Expired

Dear Customer,

Your Pitney Bowes postage meter lease and SendPro subscription has expired. You are no longer able to print postage or shipping labels using your device.

To renew your subscription and avoid service interruption:
https://pitney-bowes-renew.com/subscription

During the lapse period, any mail sent without valid postage may be returned. Please renew within 72 hours to restore your meter functionality and avoid a reconnection fee.

Pitney Bowes Subscription Services""",

    """Subject: Maersk: Your Container Shipment Is Being Held — Port Storage Fee Due

Dear Shipper,

Your Maersk container (Bill of Lading: MAEU123456789) arrived at the Port of Los Angeles but cannot be released due to an outstanding demurrage (port storage) fee of $892.00.

Containers not retrieved within 5 free days accrue daily storage fees. Your container has exceeded the free period.

Pay demurrage fee and schedule pickup:
https://maersk-demurrage-pay.com/release-container

If the fee is not paid within 48 hours, your container will be moved to long-term storage and additional fees will apply.

Maersk Line Customer Operations""",

    """Subject: LaserShip: Your Package Could Not Be Delivered — Address Issue

Dear Customer,

LaserShip attempted to deliver your package today but was unable to complete delivery due to an address discrepancy. Your package is now being held at our regional facility.

To update your delivery address and reschedule:
https://lasership-address-update.com/reschedule

Your package details:
Tracking #: 1LS23814920047
Retailer: Online Fashion Retailer
Estimated Value: $67.00

If redelivery is not scheduled within 3 business days, the package will be returned to the retailer.

LaserShip Delivery Support""",

    """Subject: ShipBob: Your Order Fulfillment Is On Hold — Payment Failed

Dear Merchant,

Your ShipBob fulfillment account has a failed payment of $1,482.00 for order fulfillment services. All pending shipments have been placed on hold until the outstanding balance is resolved.

To release your orders and resume fulfillment:
https://shipbob-billing-resolve.com/pay-balance

Your customers' orders will be delayed until payment is processed. We recommend notifying your customers of the delay to maintain satisfaction ratings.

ShipBob Merchant Services""",

    """Subject: Uber Eats: Your Restaurant Order Was Incorrectly Prepared — Refund Available

Dear Uber Eats Customer,

Your recent Uber Eats order (#UE-58291740) was reported as incorrectly prepared. One or more items did not match your order or were missing. A refund of $24.99 is available.

Claim your refund now: https://ubereats-refund-claim.com/order-issue

Your refund can be applied as Uber Cash (instant) or returned to your original payment method (3–5 business days). This offer is valid for 48 hours.

Uber Eats Customer Support""",

    """Subject: DoorDash: Dashpass Membership — Payment Failed, Benefits Ending

Dear DoorDash Customer,

The payment for your DashPass membership failed. Your DashPass benefits — including $0 delivery fees and reduced service fees — will be suspended in 24 hours.

Update your payment to keep your DashPass benefits:
https://doordash-dashpass-billing.com/update-payment

As a DashPass member, you save an average of $4–5 per order. Updating your payment now ensures uninterrupted savings on every DoorDash order.

DoorDash Billing Support""",

]

# =============================================================================
# CATEGORY 4 — GOVERNMENT / OFFICIAL NOTICES (15 emails)
# New agencies and scenarios
# =============================================================================
GOVERNMENT_NEW = [

    """Subject: State Tax Authority: Your State Tax Return Has Been Flagged for Review

Dear Taxpayer,

Your state income tax return for the most recent tax year has been selected for review by the State Department of Revenue. A discrepancy was identified between your reported income and information provided by third parties.

To respond to this review and avoid an assessment:
https://state-tax-review-response.com/submit-documents

You have 30 days to provide supporting documentation. Failure to respond may result in an automatic assessment of additional taxes, penalties, and interest.

State Department of Revenue — Compliance Division""",

    """Subject: DMV: Your Vehicle Registration Will Be Revoked in 72 Hours

Dear Vehicle Owner,

Our records indicate that your vehicle registration has expired and you have not renewed within the grace period. Continued operation of an unregistered vehicle is a violation of state law and may result in your vehicle being impounded.

Renew your registration online immediately:
https://dmv-registration-renew.com/online-renewal

Online renewal is available 24/7 and takes less than 5 minutes. Once renewed, your updated registration sticker will be mailed within 7–10 business days.

Department of Motor Vehicles""",

    """Subject: Jury Duty Summons: Failure to Report May Result in Contempt Charges

Dear Citizen,

You have been summoned to report for jury duty. Our records indicate you failed to appear on your scheduled date. Failure to appear for jury duty is a civil contempt of court and may result in a fine of up to $1,500.

To respond to this summons and avoid contempt charges:
https://court-jury-duty-response.com/respond-online

You may request a postponement, deferral, or exemption through the online portal. All requests must be submitted at least 48 hours before your rescheduled date.

Office of the Court Clerk
Federal District Court""",

    """Subject: U.S. Passport Agency: Your Passport Renewal Application Requires Action

Dear Applicant,

Your U.S. Passport renewal application (#PP-2024-48291) is on hold. Additional documentation is required to complete processing. If the required documents are not submitted within 21 days, your application will be cancelled and your fees forfeited.

Submit your supporting documents:
https://passport-renewal-documents.com/upload

Required documents: Proof of U.S. citizenship, government-issued photo ID, and two passport-quality photos. Expedited processing is available for an additional fee if you have imminent international travel.

U.S. Passport Services""",

    """Subject: VA Benefits: Your Disability Compensation Payment Is on Hold

Dear Veteran,

The Department of Veterans Affairs has placed your monthly disability compensation payment on hold pending verification of your continued eligibility. This is a routine review required every 3 years.

To confirm your eligibility and release your payment:
https://va-disability-verify.com/eligibility-confirm

Your payment will be released within 3 business days of successful verification. Missing more than one payment cycle may require a formal redetermination by a VA adjudicator.

U.S. Department of Veterans Affairs
Veterans Benefits Administration""",

    """Subject: TSA PreCheck: Your Known Traveler Number Has Expired

Dear Traveler,

Your TSA PreCheck Known Traveler Number (KTN) expired this month. You are no longer eligible for PreCheck screening lanes. You must complete the renewal process to restore PreCheck benefits.

Renew your TSA PreCheck membership:
https://tsa-precheck-renew.com/renewal-application

Renewal requires identity verification and a background check update. Processing typically takes 3–5 weeks. A fee of $85 applies for 5-year membership renewal.

Transportation Security Administration""",

    """Subject: Unemployment Insurance: Overpayment Notice — Repayment Required

Dear Claimant,

A review of your unemployment insurance claim (#UI-2024-88291) has determined that you received an overpayment of $1,847.00. This overpayment occurred due to unreported income during your benefit period.

To repay this amount and avoid collection action:
https://unemployment-overpayment-repay.com/make-payment

If repayment is not made within 30 days, the amount will be referred to the state collections agency and may affect your ability to receive future unemployment benefits.

State Unemployment Insurance Division""",

    """Subject: REAL ID Compliance Notice: Your ID Will Not Be Accepted at Airports

Dear State Resident,

Beginning May 7, 2025, TSA will require a REAL ID-compliant driver's license or identification card to board domestic flights. Our records indicate your current ID is not REAL ID-compliant.

To upgrade to a REAL ID before the deadline:
https://realid-compliance-upgrade.com/schedule-appointment

You will need to visit your local DMV with: proof of identity (passport or birth certificate), proof of Social Security number, and two proofs of state residency. Schedule your appointment early as DMV offices are experiencing high demand.

Department of Homeland Security — REAL ID Program""",

    """Subject: FEMA: You Are Eligible for Disaster Assistance — Claim Expires Soon

Dear Resident,

Federal Emergency Management Agency records indicate you may be eligible for disaster assistance following the recent federally declared disaster in your area. Your registration window closes in 7 days.

Register for assistance:
https://fema-disaster-assistance.com/register-now

Eligible assistance includes: temporary housing, home repair grants, and personal property replacement. Most applicants receive an initial determination within 10 days of registration.

FEMA Individual Assistance Program""",

    """Subject: SBA: Your Economic Injury Disaster Loan Application Requires Documents

Dear Business Owner,

Your Small Business Administration Economic Injury Disaster Loan application (#SBA-EIDL-2024-3827) is incomplete. Additional documentation must be submitted within 14 days or your application will be withdrawn.

Upload your documents:
https://sba-eidl-documents.com/upload

Required documents: Recent business tax returns, profit and loss statements for the past 12 months, and a current balance sheet. Loans of up to $2 million are available at low interest rates.

SBA Disaster Loan Servicing Center""",

    """Subject: Medicare: Your Annual Wellness Visit Authorization Has Expired

Dear Medicare Beneficiary,

Your authorization for a Medicare Annual Wellness Visit has expired. Without a renewed authorization, your healthcare provider may bill you directly for this service, which is normally covered at no cost.

Renew your Medicare authorization:
https://medicare-wellness-auth.com/renew

This visit helps your doctor update your personalized prevention plan and screen for health risks at no cost to you. Please renew your authorization before scheduling your next visit.

Centers for Medicare & Medicaid Services""",

    """Subject: Property Tax Notice: Delinquent Tax Lien — Final Notice Before Sale

Dear Property Owner,

Your property tax account shows an outstanding balance of $3,892.00 including penalties and interest. This account is 18 months delinquent and has been scheduled for tax lien sale.

To redeem your property and prevent lien sale:
https://property-tax-lien-redeem.com/pay-now

Payment must be received in full within 10 business days. Failure to pay will result in a tax lien being sold to a third-party investor, who may then foreclose on your property.

County Tax Collector's Office""",

    """Subject: Food Stamps (SNAP): Your EBT Card Has Been Temporarily Suspended

Dear SNAP Recipient,

Your Electronic Benefits Transfer (EBT) card has been temporarily suspended due to suspicious activity on your account. To protect your benefits, we have blocked card transactions until your identity is verified.

Verify your identity and restore your EBT card:
https://snap-ebt-verify.com/restore-card

Your SNAP benefits remain available and will be accessible once your card is restored. Please verify your identity as soon as possible to avoid missing your monthly benefits.

State Department of Social Services — SNAP Program""",

    """Subject: USCIS: Your Immigration Case Requires Additional Evidence

Dear Applicant,

U.S. Citizenship and Immigration Services has reviewed your pending application and issued a Request for Evidence (RFE). You must submit the requested evidence within 87 days of the date of this notice.

Review your RFE and submit evidence:
https://uscis-rfe-response.com/submit-evidence

Failure to respond to the RFE within the deadline will result in denial of your application. Your application filing fee is non-refundable regardless of the outcome.

U.S. Citizenship and Immigration Services""",

    """Subject: State Lottery Commission: Your Lottery Prize Check Has Not Been Claimed

Dear Winner,

The State Lottery Commission has been attempting to contact you regarding an unclaimed lottery prize of $25,000.00 from a draw held last month. Prize claims expire 6 months from the draw date.

Claim your lottery prize:
https://state-lottery-claim.com/verify-ticket

To claim your prize, you must verify your identity and provide the winning ticket number. Prizes over $600 are subject to state and federal tax withholding.

State Lottery Commission — Prize Claims Department""",

]

# =============================================================================
# CATEGORY 5 — PRIZE / REWARD LURES (15 emails)
# Airline, hotel, restaurant, and retail rewards
# =============================================================================
PRIZE_NEW = [

    """Subject: Delta SkyMiles: You Have 50,000 Bonus Miles Ready to Claim

Dear Delta SkyMiles Member,

Congratulations! Your Delta SkyMiles account has been selected to receive 50,000 bonus miles as part of our Customer Appreciation promotion. These miles are enough for a round-trip domestic flight!

Claim your bonus miles: https://delta-skymiles-bonus.com/claim-miles

Your bonus miles will be deposited into your SkyMiles account within 24 hours of claiming. Miles expire 24 months from the date of last account activity.

Delta Air Lines SkyMiles Program""",

    """Subject: Marriott Bonvoy: Your Points Are About to Expire — Act Now

Dear Marriott Bonvoy Member,

Your Marriott Bonvoy account shows 42,000 points that are scheduled to expire at the end of this month. Expired points cannot be restored.

Redeem or extend your points:
https://marriott-bonvoy-points.com/redeem-or-extend

You can use your points for free night awards, airline miles, gift cards, or experiences. Alternatively, complete a qualifying stay to extend your points for another 24 months.

Marriott Bonvoy Member Services""",

    """Subject: Southwest Airlines: You Have a $500 Rapid Rewards Travel Credit

Dear Southwest Rapid Rewards Member,

You have been selected to receive a $500 Southwest Airlines travel credit as part of our Rapid Rewards Partner Appreciation program. This credit may be applied to any Southwest flight.

Claim your travel credit:
https://southwest-travel-credit.com/claim

Your credit is valid for 12 months from the date of issue and may be used for one or multiple Southwest flights. It cannot be combined with other promotional offers.

Southwest Airlines Rapid Rewards""",

    """Subject: Hilton Honors: 75,000 Bonus Points Waiting for You

Dear Hilton Honors Member,

Your Hilton Honors account has been selected for a special bonus of 75,000 Hilton Honors points — enough for multiple free night stays at Hilton properties worldwide.

Claim your bonus points:
https://hilton-honors-bonus.com/claim-points

Points will be added to your account within 48 hours. Use your points for free nights at Hilton, DoubleTree, Embassy Suites, Hampton Inn, and 18 other Hilton brands.

Hilton Honors Member Appreciation""",

    """Subject: CVS ExtraCare: You Have $84.50 in ExtraBucks Expiring Today

Dear ExtraCare Member,

Your CVS ExtraCare account shows $84.50 in ExtraBucks Rewards that expire at midnight tonight. Expired ExtraBucks cannot be recovered.

Redeem your ExtraBucks in-store or online:
https://cvs-extracare-redeem.com/use-extrabucks

ExtraBucks can be used toward most CVS purchases including prescriptions, beauty products, vitamins, and household items. Visit any CVS location or use them at CVS.com.

CVS ExtraCare Rewards""",

    """Subject: Walgreens Balance Rewards: Your Points Are Expiring

Dear Balance Rewards Member,

Your Walgreens Balance Rewards account has 18,500 points (equivalent to $18.50) that are set to expire at the end of this month. Expired points cannot be reinstated.

Redeem your points online or in-store:
https://walgreens-balance-rewards.com/redeem

Points can be redeemed toward most Walgreens purchases. Use your myWalgreens card at checkout and select the number of points you'd like to apply.

Walgreens Balance Rewards Program""",

    """Subject: Chick-fil-A: You Have a Free Sandwich Reward — Expires Tomorrow

Dear Chick-fil-A One Member,

Your Chick-fil-A One account has a complimentary Chick-fil-A Chicken Sandwich reward that expires tomorrow at 11:59 PM. Expired rewards cannot be restored.

Use your reward at any Chick-fil-A location:
https://chickfila-reward-claim.com/use-reward

Simply show this QR code at the counter or drive-thru to redeem your free sandwich. Valid at participating Chick-fil-A locations only.

Chick-fil-A One Membership""",

    """Subject: Subway: You've Earned a Free Footlong Sub — Claim Before It Expires

Dear Subway MVP Rewards Member,

You've earned enough points for a Free Footlong Sub! Your reward is available but will expire in 48 hours if not redeemed.

Redeem at any participating Subway:
https://subway-mvp-rewards.com/free-footlong

Choose any 6-inch or footlong sandwich, wrap, or salad. Valid at participating Subway locations in the U.S. Cannot be combined with other offers.

Subway MVP Rewards Program""",

    """Subject: Dunkin: Your DD Perks Rewards Are Expiring — Free Drink Inside

Dear DD Perks Member,

You have a free medium beverage reward in your Dunkin' DD Perks account that expires in 24 hours. Don't miss your free coffee, tea, or latte!

Claim your free drink: https://dunkin-perks-reward.com/free-drink

Scan your app at any participating Dunkin' location to redeem. Valid for any medium hot, iced, or frozen beverage. Not valid with any other offer.

Dunkin' DD Perks""",

    """Subject: American Airlines AAdvantage: Your Miles Are Expiring in 7 Days

Dear AAdvantage Member,

Your American Airlines AAdvantage miles will expire in 7 days due to account inactivity. You have 38,000 miles at risk of expiration — enough for a round-trip award flight.

Prevent your miles from expiring:
https://aa-aadvantage-miles.com/prevent-expiration

To prevent expiration, you must complete a qualifying activity such as a flight, credit card purchase, or partner transaction. Alternatively, purchase miles to extend your account activity.

American Airlines AAdvantage Customer Service""",

    """Subject: Shell Fuel Rewards: You Have $0.60/gal Reward About to Expire

Dear Fuel Rewards Member,

Your Shell Fuel Rewards account has a Gold Status reward of $0.60 per gallon that expires at the end of this month. Use it now to save on your next fill-up.

Redeem your fuel discount: https://shell-fuel-rewards.com/redeem-discount

Visit any participating Shell station and swipe your Fuel Rewards card or enter your phone number at the pump to apply your discount. Maximum 20 gallons per transaction.

Shell Fuel Rewards Network""",

    """Subject: IHOP Rewards: You Have a Free Stack of Pancakes Waiting

Dear IHOP Rewards Member,

Your IHOP Rewards account has a complimentary short stack of pancakes reward that has not been redeemed. This reward expires in 3 days.

Redeem at any IHOP location: https://ihop-rewards-pancakes.com/redeem

Show your reward barcode to your server when placing your order. Valid for dine-in only. Cannot be combined with any other offer or discount.

IHOP International House of Pancakes""",

    """Subject: Olive Garden: Your eClub Birthday Reward Is About to Expire

Dear Olive Garden eClub Member,

Your Olive Garden eClub birthday reward — a complimentary appetizer or dessert — expires in 48 hours. This reward is available to all eClub members during their birthday month.

Use your birthday reward: https://olivegarden-eclub.com/birthday-reward

Present this reward at any Olive Garden location to redeem your complimentary appetizer or dessert with the purchase of any adult entree. Dine-in only.

Olive Garden eClub Rewards""",

    """Subject: Dollar General: You Have $20 in DG Digital Coupons Expiring Today

Dear DG Rewards Member,

Your Dollar General DG Rewards account has $20.00 in digital coupons that expire at midnight tonight. These coupons are applied automatically at checkout when you use your DG Rewards account.

Shop in-store or online before midnight:
https://dollargeneral-rewards.com/use-coupons

Your coupons cover everyday essentials including cleaning supplies, paper products, snacks, and personal care items. Visit your nearest Dollar General or shop at DGPickup.com.

Dollar General DG Rewards""",

    """Subject: United Airlines MileagePlus: 30,000 Bonus Miles — Limited Time Offer

Dear MileagePlus Member,

Your United Airlines MileagePlus account has been selected to receive 30,000 bonus miles as part of our Explorer Member promotion. These miles never expire as long as your account is active.

Claim your bonus miles:
https://united-mileageplus-bonus.com/claim

30,000 MileagePlus miles is enough for a roundtrip award flight within the continental United States. Miles will be credited to your account within 72 hours of claiming.

United Airlines MileagePlus""",

]

# =============================================================================
# CATEGORY 6 — HR / PAYROLL (15 emails)
# New workplace scenarios
# =============================================================================
HR_NEW = [

    """Subject: IT Migration Notice: Your Company Email Will Be Deactivated

Dear Employee,

As part of our company's transition to Microsoft 365, all legacy email accounts will be deactivated on Friday at 5:00 PM. Employees must complete the migration before this deadline to retain access to their emails and contacts.

Complete your email migration:
https://company-email-migration.com/setup-new-account

After the migration, you will use your new Microsoft 365 email address for all company communications. Your old emails will be imported automatically. Contact IT support at extension 2200 for assistance.

IT Department — Migration Team""",

    """Subject: HR: Your Background Check Results Require Your Attention

Dear Team Member,

As part of our annual compliance review, a background check was conducted on your employment record. The results require your review and response within 5 business days.

Review your background check results:
https://hr-background-check.com/employee-review

You have the right to dispute any inaccurate information in your background check. If you believe any information is incorrect, please submit a dispute through the portal.

Human Resources — Compliance""",

    """Subject: COBRA: Your Health Insurance Coverage Has Lapsed — Elect Now

Dear Former Employee,

Your employer-sponsored health insurance coverage terminated with your employment. You have 60 days from your termination date to elect COBRA continuation coverage. Your COBRA election window closes this week.

Elect COBRA coverage now: https://cobra-election-portal.com/elect-coverage

COBRA coverage provides continuation of your existing health, dental, and vision insurance. Premium payments are due within 45 days of election. Retroactive coverage is available once premiums are paid.

COBRA Administration Services""",

    """Subject: Paylocity: Your Pay Stub Is Ready — Login Required

Dear Employee,

Your most recent pay stub is now available in the Paylocity employee self-service portal. Due to a system migration, you must re-verify your account to access your pay stub and tax documents.

Access your pay stub: https://paylocity-employee-portal.com/re-verify

Your W-2 and year-to-date earnings summary are also available in the portal. If you experience any issues, contact your HR administrator or Paylocity support.

Paylocity HR & Payroll""",

    """Subject: Annual Compliance Training: Incomplete — Account Will Be Flagged

Dear Team Member,

Our records show that you have not completed your required annual compliance training, which was due last Friday. Employees who have not completed mandatory training will be flagged in the HR system and may be ineligible for their annual merit increase.

Complete your training now:
https://compliance-training-portal.com/complete-training

Courses required: Code of Conduct (30 min), Data Privacy Awareness (20 min), Cybersecurity Basics (25 min). Total estimated time: 75 minutes.

HR Learning & Development""",

    """Subject: Stock Options: Your Unvested Options Will Be Forfeited at Month End

Dear Employee,

Our records indicate that 2,500 unvested stock options from your original grant are scheduled to vest this month, but you have not logged into the equity management portal to accept them. Unclaimed options are forfeited after 30 days.

Access your equity portal and accept your options:
https://equity-portal-access.com/accept-options

The current estimated value of your vesting options is approximately $18,750 based on today's share price. Please contact your HR Business Partner if you have questions about your equity grant.

HR Equity & Compensation""",

    """Subject: FMLA Paperwork: Your Leave Request Requires Additional Documentation

Dear Employee,

Your Family and Medical Leave Act (FMLA) request (#FMLA-2024-8821) is on hold pending receipt of completed medical certification from your healthcare provider. Your leave cannot be approved until this documentation is received.

Submit your medical certification:
https://fmla-documentation-portal.com/upload-certification

Your healthcare provider must complete the Department of Labor's WH-380 form. The form must be returned within 15 calendar days. FMLA protections do not apply until your leave is formally approved.

Human Resources — Leave Administration""",

    """Subject: Expense Report: Reimbursement Pending — Receipt Submission Required

Dear Team Member,

Your expense report (#ER-2024-4892) totaling $847.20 has been approved but reimbursement is on hold. Receipts for 3 line items are missing or illegible and must be resubmitted before payment can be processed.

Resubmit your receipts: https://expense-report-resubmit.com/upload

Reimbursements are processed every Friday. Receipts received by Wednesday will be included in this week's payment cycle. Late submissions will be processed in the following cycle.

Finance — Accounts Payable""",

    """Subject: Employee Handbook Update: You Must Acknowledge the New Policies

Dear Employee,

Our updated Employee Handbook and Code of Conduct became effective on the 1st of this month. All employees are required to read and electronically acknowledge the updated policies within 10 business days.

Acknowledge the new policies: https://hr-policy-acknowledgment.com/sign

Key policy updates include: remote work guidelines, expense reimbursement limits, social media policy, and non-disclosure agreement revisions. Your acknowledgment is a condition of continued employment.

Human Resources — Policy Administration""",

    """Subject: 401(k) Auto-Enrollment: You Have Been Enrolled — Change Your Rate

Dear New Employee,

As a benefit of your employment, you have been automatically enrolled in the company 401(k) plan at a contribution rate of 3% of your gross salary. Contributions begin with your next paycheck.

To change your contribution rate or opt out:
https://401k-enrollment-portal.com/manage-contributions

The company matches 100% of your contributions up to 4% of your salary. We strongly recommend contributing at least 4% to receive the full company match. Changes take effect within two pay periods.

Benefits Administration — 401(k) Program""",

    """Subject: DocuSign: Your Employment Contract Amendment Requires Signature

Dear Employee,

An amendment to your employment agreement has been prepared following the recent organizational restructuring. This document requires your electronic signature by end of business on Friday.

Review and sign your amendment:
https://docusign-employment-amendment.com/sign?id=emp-2024-8832

The amendment covers updates to your role description, reporting structure, and remote work eligibility. Please review the document carefully and contact HR with any questions before signing.

DocuSign via HR Legal and Compliance""",

    """Subject: ADP Workforce Now: Your Time Off Balances Are Being Adjusted

Dear Employee,

As part of our transition to a new PTO policy, your accrued vacation and sick leave balances are being adjusted in ADP Workforce Now. You must log in and confirm your balances before the adjustment is finalized.

Confirm your PTO balances: https://adp-workforce-pto.com/confirm-balances

Balances that are not confirmed by end of month will be automatically adjusted per the new policy. Any discrepancies must be reported to your HR Business Partner within 30 days.

ADP Workforce Now — HR Administration""",

    """Subject: Remote Work Equipment: Your Laptop Return Is Overdue

Dear Employee,

Our IT Asset Management records show that your company-issued laptop and peripheral equipment have not been returned following your separation from the company. The outstanding equipment value is $2,340.00.

To arrange a return shipping label:
https://it-equipment-return.com/schedule-return

Failure to return company equipment within 30 days of separation may result in deduction from your final paycheck or referral to collections. Please coordinate with IT at assets@company.com.

IT Asset Management""",

    """Subject: Gusto Payroll: Your Banking Information Could Not Be Verified

Dear Employee,

Your direct deposit banking information in Gusto could not be verified with your bank. Your upcoming paycheck will be held until your banking information is re-verified.

Update your banking information:
https://gusto-payroll-banking.com/update-bank

Please update your routing and account numbers as soon as possible. If your information is not updated by the next payroll run, your paycheck will be issued as a paper check and mailed to your address on file.

Gusto Payroll Support""",

    """Subject: Severance Package Offer: Your Response Is Required Within 5 Days

Dear Employee,

As part of the recent reduction in force, you have been selected to receive a severance package. To receive severance pay, you must review, sign, and return the Separation Agreement and General Release within 5 business days.

Review and accept your severance offer:
https://severance-offer-portal.com/review-agreement

Your severance package includes: 8 weeks of base salary, continuation of health benefits for 60 days, and outplacement services. You have 21 days to consider this offer and 7 days to revoke after signing.

Human Resources — Employee Relations""",

]

# =============================================================================
# CATEGORY 7 — HEALTHCARE / INSURANCE (15 emails)
# New providers and scenarios
# =============================================================================
HEALTHCARE_NEW = [

    """Subject: Your Prescription Is Ready for Pickup — Action Required

Dear Patient,

Your prescription for a 90-day supply has been filled at your pharmacy and is ready for pickup. Your prescription will be returned to stock if not picked up within 7 days.

Confirm your pickup or request mail delivery:
https://pharmacy-prescription-ready.com/confirm-pickup

If you have questions about your medication, a licensed pharmacist is available for consultation. To request home delivery instead, select the mail delivery option and your prescription will ship within 2 business days.

Pharmacy Patient Services""",

    """Subject: Cigna: Prior Authorization Required for Your Upcoming Procedure

Dear Cigna Member,

Our records indicate that your upcoming medical procedure scheduled for next week requires prior authorization that has not yet been obtained. Without authorization, the procedure may not be covered by your plan.

Submit for prior authorization:
https://cigna-prior-auth.com/submit-request

Your healthcare provider must submit the authorization request along with supporting clinical documentation. Processing takes 2–5 business days. Urgent requests may be expedited.

Cigna Healthcare — Prior Authorization Department""",

    """Subject: Kaiser Permanente: Your Lab Results Are Ready to View

Dear Kaiser Permanente Member,

Your recent lab results are now available in your Kaiser Permanente kp.org health record. Some results may require follow-up with your care team.

View your lab results: https://kaiser-permanente-results.com/view-labs

If you have questions about your results, you may send a secure message to your doctor through your online health record or call Member Services to schedule a follow-up appointment.

Kaiser Permanente Member Services""",

    """Subject: Blue Shield: Your Referral Authorization Has Expired

Dear Blue Shield Member,

Your referral authorization to see a specialist (Referral #: BS-2024-58291) has expired. Without a valid referral, services provided by your specialist may not be covered under your Blue Shield plan.

Request a new referral: https://blueshield-referral-renew.com/request

Your primary care physician must submit a new referral request. Referrals are valid for 90 days from the date of issue. Services rendered without a valid referral may be billed at out-of-network rates.

Blue Shield Member Services""",

    """Subject: Humana Medicare Advantage: Your Annual Notice of Change

Dear Humana Member,

Your Humana Medicare Advantage plan benefits are changing effective January 1st. Your monthly premium, copayments, and covered services may be different from what you currently pay.

Review your Annual Notice of Change:
https://humana-medicare-anoc.com/review-changes

You have until December 7th to switch Medicare Advantage plans or return to Original Medicare if the changes do not meet your needs. Contact a licensed Humana agent for personalized guidance.

Humana Medicare Member Communications""",

    """Subject: VSP Vision: Your Vision Benefits Expire December 31 — Use Them Now

Dear VSP Vision Care Member,

Your VSP vision benefits expire at the end of this year. Unused benefits do not roll over. Your plan covers one comprehensive eye exam and allowances for frames or contact lenses.

Schedule your exam and use your benefits:
https://vsp-vision-benefits.com/find-provider

Use our provider locator to find a VSP network doctor near you. Most exams can be scheduled within 1–2 weeks. Contact lens fittings and evaluations require a separate appointment.

VSP Vision Care Member Benefits""",

    """Subject: Delta Dental: Your Dental Claim Has Been Denied — Appeal Available

Dear Delta Dental Member,

Your dental claim (#DD-2024-892847) for a crown procedure has been denied. The denial reason is: service not covered under your current benefit plan. You have the right to appeal this decision.

Submit your appeal:
https://deltadental-claim-appeal.com/submit-appeal

Your appeal must be submitted within 180 days of the denial date. Include a letter of medical necessity from your dentist and any supporting X-rays or treatment records. Appeal decisions are made within 30 days.

Delta Dental Claims and Appeals""",

    """Subject: Express Scripts: Your Mail-Order Prescription Is Running Low

Dear Express Scripts Member,

Our records show that your 90-day mail-order prescription for a maintenance medication will run out in approximately 14 days. Please reorder now to avoid a gap in treatment.

Reorder your prescription:
https://express-scripts-reorder.com/refill-now

Your copay for this refill is $45.00 under your current plan. If your prescription has expired, your doctor must submit a new prescription before we can process your refill.

Express Scripts Pharmacy Services""",

    """Subject: Teladoc: Your Virtual Visit Appointment Confirmation Needed

Dear Teladoc Member,

You have a scheduled Teladoc virtual visit in 24 hours. To confirm your appointment and ensure your video connection is working, please verify your contact information.

Confirm your Teladoc appointment:
https://teladoc-appointment-confirm.com/verify

Before your visit, please have your insurance card, list of current medications, and a list of symptoms or questions ready. Teladoc visits are $0 copay under most insurance plans.

Teladoc Health Patient Services""",

    """Subject: LabCorp: Your Test Results Require Urgent Follow-Up

Dear Patient,

Your recent LabCorp lab test results are available in your patient portal. One or more results fall outside the normal reference range and may require follow-up with your healthcare provider.

View your results and contact your doctor:
https://labcorp-results-portal.com/view-urgent

Your doctor has been notified of your results. We recommend scheduling a follow-up appointment as soon as possible. Call your doctor's office if you have not heard from them within 24 hours.

LabCorp Patient Services""",

    """Subject: Aetna: Your Health Plan Renewal Requires Your Action

Dear Aetna Member,

Your Aetna health insurance plan is up for renewal. Your current plan will not automatically renew unless you take action before the open enrollment deadline.

Review and renew your plan: https://aetna-plan-renewal.com/review-options

During open enrollment, you may keep your current plan, switch to a different Aetna plan, or change your coverage level. Premium changes for the coming year are outlined in your renewal packet.

Aetna Member Services — Open Enrollment""",

    """Subject: FSA Balance Alert: $487.00 Will Be Forfeited at Year End

Dear FSA Account Holder,

Your Flexible Spending Account has a remaining balance of $487.00 that must be spent before December 31. FSA funds are use-it-or-lose-it — any unspent balance will be forfeited.

Use your FSA balance now: https://fsa-balance-spend.com/eligible-expenses

Eligible FSA expenses include prescriptions, eyeglasses, dental work, medical equipment, and over-the-counter medications. Your FSA debit card can be used at most pharmacies and healthcare providers.

FSA Plan Administrator""",

    """Subject: UnitedHealthcare: Your Out-of-Network Bill Has Been Resolved

Dear UnitedHealthcare Member,

Your disputed out-of-network medical bill (#UHC-2024-48291) has been reviewed and resolved through our No Surprises Act arbitration process. You owe a reduced amount of $187.00 instead of the original $1,842.00 billed.

View and pay your resolved bill:
https://uhc-bill-resolution.com/pay-balance

This amount must be paid within 30 days to avoid the account being sent to collections. If you believe this resolution is incorrect, you may request a secondary review within 60 days.

UnitedHealthcare Member Billing""",

    """Subject: Molina Healthcare: Your Medicaid Plan May Be Affected by Renewal

Dear Molina Healthcare Member,

States are reviewing Medicaid eligibility for all enrolled members following the end of the continuous enrollment period. Your Medicaid coverage may be terminated if you do not complete your renewal.

Complete your Medicaid renewal:
https://molina-medicaid-renewal.com/renew-coverage

You should have received a renewal form in the mail. If you did not receive your form or need assistance completing it, please contact your state Medicaid office or call Molina Member Services.

Molina Healthcare Member Services""",

    """Subject: Optum Rx: Your Prior Authorization for Specialty Medication Is Expiring

Dear Optum Rx Member,

The prior authorization for your specialty medication expires in 7 days. Without a renewed authorization, your prescription will not be covered and you will be responsible for the full cost, which may exceed $2,000 per month.

Request your prior authorization renewal:
https://optumrx-prior-auth.com/renew

Your prescribing physician must submit the renewal request along with updated clinical documentation. Processing takes up to 72 hours. Contact Optum Rx Specialty Pharmacy at the number on your insurance card.

Optum Rx Specialty Pharmacy Services""",

]

# =============================================================================
# CATEGORY 8 — SOCIAL MEDIA / TRAVEL / JOB OFFERS (15 emails)
# New attack vectors not in original 200
# =============================================================================
SOCIAL_TRAVEL_JOB = [

    """Subject: Facebook: Your Account Has Been Disabled for Policy Violations

Dear Facebook User,

Your Facebook account has been disabled following a review that found content violating our Community Standards. All access to your account, including Messenger, Marketplace, and connected apps, has been suspended.

To appeal this decision: https://facebook-account-appeal.com/dispute

You have 30 days to submit an appeal. If no appeal is submitted, your account and all associated data will be permanently deleted. Facebook takes violations of our Community Standards seriously.

Facebook Trust & Safety""",

    """Subject: Instagram: Verify Your Account to Keep Your Blue Checkmark

Dear Instagram Creator,

Your verified Instagram account is at risk of losing its blue verification badge due to a recent policy update requiring all verified accounts to re-confirm their identity.

Re-verify your account now: https://instagram-verified-reconfirm.com/verify

Failure to re-verify within 7 days will result in automatic removal of your verified badge. Re-verification requires a government-issued ID and confirmation of your account details.

Instagram Verification Team""",

    """Subject: LinkedIn: You Have a Job Offer Waiting — Expires in 48 Hours

Dear LinkedIn Member,

A recruiter from a Fortune 500 company has sent you a direct job offer through LinkedIn Recruiter. This is a confidential executive-level opportunity. The offer expires in 48 hours.

View your job offer: https://linkedin-job-offer.com/view-opportunity

The position offers a base salary of $185,000 with equity and full benefits. The recruiter has specifically selected your profile based on your experience. Log in to review the full job description and compensation package.

LinkedIn Talent Solutions""",

    """Subject: TikTok: Your Creator Fund Payment Is Being Held

Dear TikTok Creator,

Your TikTok Creator Fund payment of $342.00 has been placed on hold pending identity verification. This is required for all Creator Fund payments exceeding $100.

Complete your identity verification:
https://tiktok-creator-fund-verify.com/verify-identity

You will need to submit a government-issued photo ID and confirm your payment information. Payments are released within 3 business days of successful verification.

TikTok Creator Support""",

    """Subject: Airbnb: Your Host Payout Has Been Delayed — Action Required

Dear Airbnb Host,

Your upcoming host payout of $1,247.00 for 3 recent reservations has been delayed. Our payment system flagged your payout for manual review due to a change in your payout method.

Verify your payout information: https://airbnb-host-payout.com/verify-account

To release your payment, please confirm your bank account details and re-verify your government-issued ID. Payments are released within 2–3 business days of verification.

Airbnb Host Support""",

    """Subject: Expedia: Your Reservation Has Been Cancelled — Act Now for a Refund

Dear Expedia Customer,

Your hotel reservation (Booking #: EXP-2024-89201) has been cancelled by the property due to an overbooking situation. We sincerely apologize for this inconvenience.

To rebook or request a full refund:
https://expedia-cancellation-refund.com/rebook-or-refund

We will provide a full refund to your original payment method within 5–7 business days. Alternatively, we can assist you in finding a comparable hotel at the same price. Expedia guarantees you will not pay more than the original rate.

Expedia Customer Service""",

    """Subject: United Airlines: Your Flight Has Been Cancelled — Rebook Now

Dear United Airlines Customer,

Your United Airlines flight (UA-1482, departing tomorrow at 7:30 AM) has been cancelled due to operational issues. We apologize for this disruption to your travel plans.

Rebook your flight or request a refund:
https://united-flight-rebook.com/options

You may rebook on any available United flight at no additional charge, or request a full refund to your original payment method. MileagePlus members may also opt for a miles credit.

United Airlines Customer Care""",

    """Subject: Marriott: Your Reservation Requires Immediate Credit Card Verification

Dear Marriott Guest,

Your upcoming reservation at a Marriott property requires verification of the credit card on file. Our system was unable to pre-authorize your card for the estimated charges.

Verify your payment method:
https://marriott-reservation-verify.com/update-card

If your payment is not verified 24 hours before your check-in date, your reservation may be cancelled. Please ensure your credit card has sufficient available credit to cover your stay.

Marriott Hotels & Resorts Reservations""",

    """Subject: Lyft: Your Driver Account Has Been Temporarily Deactivated

Dear Lyft Driver,

Your Lyft driver account has been temporarily deactivated following a complaint from a recent passenger. During this deactivation, you are unable to accept ride requests or earn on the Lyft platform.

To appeal your deactivation:
https://lyft-driver-appeal.com/submit-appeal

Your appeal will be reviewed within 3–5 business days. During the review period, earnings from completed rides will still be paid out on your regular payment schedule.

Lyft Driver Support""",

    """Subject: Indeed: Your Job Application Was Viewed — Complete Your Profile

Dear Indeed Job Seeker,

A hiring manager at a company has viewed your resume and is interested in your application. To be considered, you must complete your Indeed profile with your most recent work experience and skills.

Complete your profile: https://indeed-profile-complete.com/update-resume

Candidates with complete profiles are 3x more likely to be contacted for an interview. Your profile completion will also make you eligible for Indeed's Apply Directly program.

Indeed Career Center""",

    """Subject: ZipRecruiter: You Have 12 New Job Matches — Salary Up to $120K

Dear ZipRecruiter Member,

Based on your recent job searches, you have 12 new job matches in your area. Several employers are actively looking for candidates with your experience and are offering salaries up to $120,000.

View your job matches: https://ziprecruiter-job-matches.com/view-matches

Act quickly — many of these positions are looking to fill within the next 2 weeks. Apply with one click using your ZipRecruiter profile. No cover letter required for most positions.

ZipRecruiter Job Alert""",

    """Subject: Work From Home Opportunity: $5,000/Month — Limited Openings

Dear Applicant,

Congratulations! After reviewing your online profile, you have been pre-selected for a remote data entry position with our company. This position offers $5,000/month working from home on a flexible schedule.

To secure your position, you must complete a background screening and pay a one-time registration fee of $49.99 to access our proprietary work platform.

Accept your offer and register: https://remote-work-offer.com/register-now

All training materials and equipment are provided. Your first paycheck is issued within 7 days of completing your first assignment. Limited openings available — act today.

Remote Opportunities Staffing Group""",

    """Subject: Pinterest: Your Creator Account Has Been Suspended

Dear Pinterest Creator,

Your Pinterest Creator account has been suspended due to pins that violate our Spam and Misinformation Policy. All your boards, pins, and follower connections have been hidden from public view.

Appeal your suspension: https://pinterest-creator-appeal.com/dispute

If you believe this suspension was made in error, you may submit an appeal with a written explanation within 30 days. If no appeal is received, your account and all associated content will be permanently deleted.

Pinterest Trust & Safety""",

    """Subject: Vrbo: Your Vacation Rental Listing Has Been Suspended

Dear Vrbo Host,

Your Vrbo vacation rental listing (#VR-2024-48920) has been suspended following guest complaints regarding the property's condition. All future bookings have been paused and guests with existing reservations have been contacted.

To restore your listing: https://vrbo-host-restore.com/appeal-suspension

You must provide documentation showing that the reported issues have been resolved. Photos and receipts for any repairs or improvements should be included with your appeal.

Vrbo Host Support""",

    """Subject: Booking.com: Your Property Reviews Are Affecting Your Ranking

Dear Property Partner,

Your property's recent guest review score has dropped below our quality threshold. Properties below this threshold are deprioritized in search results, which may significantly reduce your bookings.

Improve your property ranking: https://booking-partner-ranking.com/improve-score

To restore your ranking, you must respond to all unanswered guest reviews within 48 hours and submit a property improvement plan. Booking.com offers a free consultation with a Partner Success Manager.

Booking.com Partner Services""",

]

# =============================================================================
# CATEGORY 9 — CRYPTO / INVESTMENT / FINANCIAL FRAUD (25 emails)
# =============================================================================
CRYPTO_INVEST_NEW = [

    """Subject: Coinbase: Your Account Has Been Locked Due to Suspicious Activity

Dear Coinbase User,

Our security team has detected suspicious login activity on your Coinbase account from an unrecognized IP address in Eastern Europe. Your account has been locked to prevent unauthorized access to your cryptocurrency holdings.

Unlock your account and verify your identity:
https://coinbase-account-unlock.com/verify

Your cryptocurrency holdings are safe and unaffected. Once your identity is verified, your account will be restored within 24 hours.

Coinbase Security Operations""",

    """Subject: Binance: Mandatory KYC Upgrade Required — Account Restrictions Pending

Dear Binance User,

As part of our enhanced compliance program, all Binance users must complete a KYC (Know Your Customer) Level 2 verification by the end of this month. Accounts that do not complete the upgrade will have withdrawal and trading limits reduced to zero.

Complete your KYC upgrade: https://binance-kyc-upgrade.com/level2-verify

Required documents: government-issued photo ID, proof of residence, and a selfie with your ID. Verification typically takes 24–48 hours. Your account will be fully restored upon successful review.

Binance Compliance Department""",

    """Subject: Ethereum Wallet: Urgent — Your Wallet Has Been Compromised

Dear Wallet Holder,

Our blockchain monitoring system has detected unauthorized access to your Ethereum wallet. Multiple outgoing transactions were initiated without your authorization. Your remaining ETH balance is at risk.

Secure your wallet immediately:
https://ethereum-wallet-secure.com/emergency-lock

To prevent further unauthorized transactions, you must transfer your remaining balance to a new secure wallet address we will generate for you. Act within 2 hours to prevent total loss.

Ethereum Wallet Security Alert System""",

    """Subject: MetaMask: Your Seed Phrase May Have Been Exposed — Act Now

Dear MetaMask User,

We have received reports of a phishing campaign targeting MetaMask users in your region. If you recently entered your seed phrase on any website, your wallet may be compromised.

Verify your wallet security:
https://metamask-seed-verify.com/security-check

To confirm your wallet is secure, please enter your 12 or 24-word seed phrase in our secure verification tool. If your phrase was compromised, we will generate a new wallet and transfer your assets automatically.

MetaMask Security Team""",

    """Subject: OpenSea: Your NFT Collection Has an Offer — Verify to Accept

Dear OpenSea User,

You have received an offer of 4.2 ETH ($7,350) for your NFT collection on OpenSea. To accept this offer, you must first verify your wallet ownership through our secure portal.

Verify and accept your offer:
https://opensea-offer-accept.com/verify-wallet

This offer is valid for 48 hours. If you do not respond, the offer will be withdrawn and may not be re-submitted at the same price. The buyer has verified funds available.

OpenSea Transaction Support""",

    """Subject: Ledger: Critical Security Update Required for Your Hardware Wallet

Dear Ledger Customer,

A critical security vulnerability has been discovered in Ledger hardware wallets manufactured between 2020 and 2023. Your device may be affected. To protect your cryptocurrency, you must update your device firmware immediately.

Download the security update:
https://ledger-firmware-update.com/critical-patch

During the update process, you will be prompted to confirm your recovery phrase to ensure your funds can be restored if the update fails. This is a standard security procedure.

Ledger Security Advisory Team""",

    """Subject: Trezor: Your Hardware Wallet Requires Immediate Attention

Dear Trezor Customer,

Trezor has identified a potential vulnerability in the Trezor Model T and Trezor One firmware. As a precautionary measure, we are requiring all affected device owners to validate their wallet integrity.

Validate your wallet: https://trezor-wallet-validate.com/integrity-check

To validate, you will need to connect your Trezor device and enter your recovery seed phrase into our secure validation portal. Your funds will be temporarily moved to a secure Trezor-managed address during validation.

Trezor Security Response Team""",

    """Subject: FTX Bankruptcy Claim: Your Claim Window Is Closing

Dear Former FTX Customer,

As part of the FTX bankruptcy proceedings, affected customers are eligible to file claims for their frozen account balances. The claims filing window closes in 14 days.

File your bankruptcy claim now:
https://ftx-bankruptcy-claim.com/file-claim

To file a claim, you must provide your FTX account email, approximate account balance at time of filing, and a government-issued ID. Claims submitted after the deadline will not be considered in the distribution plan.

FTX Bankruptcy Estates Claims Administrator""",

    """Subject: BlockFi: Your Account Balance Must Be Transferred — Bankruptcy Filing

Dear BlockFi Client,

BlockFi has filed for Chapter 11 bankruptcy protection. As part of the wind-down process, all client account balances must be transferred to a designated custodial wallet by the deadline specified by the bankruptcy court.

Initiate your balance transfer:
https://blockfi-balance-transfer.com/withdraw-funds

To prevent your assets from being subject to the bankruptcy estate, you must provide a self-custody wallet address for the transfer. A small network fee will be deducted from your balance for the transfer.

BlockFi Client Recovery Program""",

    """Subject: Robinhood Crypto: Your Crypto Holdings Are Being Migrated

Dear Robinhood User,

Robinhood is migrating all cryptocurrency holdings to our new custodial infrastructure. You must opt into the migration and provide your preferred receiving wallet address before the deadline.

Opt in to the migration: https://robinhood-crypto-migrate.com/opt-in

If you do not complete the migration, your cryptocurrency holdings will be liquidated and the proceeds added to your cash balance. Migration ensures you retain full ownership of your crypto assets.

Robinhood Crypto Operations""",

    """Subject: Crypto.com: Your CRO Staking Rewards Are Ready to Claim

Dear Crypto.com Member,

Your CRO staking rewards have accumulated and are ready to be claimed. A total of 482 CRO (approximately $48.20) in staking rewards are waiting in your rewards balance.

Claim your staking rewards:
https://cryptocom-staking-claim.com/rewards

To claim your rewards, you must verify your account and confirm your staking preferences for the next cycle. Unclaimed rewards expire after 90 days and cannot be recovered.

Crypto.com Staking Program""",

    """Subject: Gemini: Your Account Has a Hold — Identity Re-Verification Required

Dear Gemini Customer,

Gemini is required by its banking partners to conduct periodic identity re-verification for all active accounts. Your account has a temporary hold on withdrawals and transfers until re-verification is complete.

Complete re-verification:
https://gemini-reverification.com/verify-identity

You will need to provide a current government-issued ID and a selfie. Re-verification typically takes 1–3 business days. Your account activity is otherwise unrestricted.

Gemini Compliance""",

    """Subject: Kraken: Your Account Password Reset Was Requested

Dear Kraken User,

A password reset was requested for your Kraken account from an IP address that does not match your usual location. If you did not request this reset, your account may be compromised.

Secure your account immediately:
https://kraken-account-secure.com/cancel-reset

To cancel the password reset and lock your account, click the link above within 30 minutes. If you do not act, the password reset will complete and the requesting party will gain access to your account.

Kraken Security Team""",

    """Subject: Uniswap: Unclaimed UNI Token Airdrop — Claim Before Expiry

Dear Ethereum Wallet Holder,

Based on your historical on-chain transaction activity, your wallet address is eligible for an unclaimed UNI governance token airdrop. The total value of your unclaimed tokens is approximately $1,840.

Claim your UNI tokens:
https://uniswap-airdrop-claim.com/claim-tokens

To claim your tokens, connect your wallet and approve the claim transaction. A small gas fee will be required to execute the on-chain transaction. This airdrop expires in 30 days.

Uniswap Protocol Governance""",

    """Subject: Celsius Network: Your Withdrawal Request Is Now Available

Dear Celsius Network Creditor,

Following the court-approved withdrawal plan in the Celsius Network bankruptcy case, creditors are now eligible to submit withdrawal requests for a portion of their frozen account balance.

Submit your withdrawal request:
https://celsius-creditor-withdrawal.com/claim-funds

To initiate your withdrawal, you must verify your identity and provide a self-custody wallet address. A 5% processing fee will be applied to all withdrawals under the bankruptcy settlement plan.

Celsius Network Bankruptcy Creditor Program""",

    """Subject: Voyager Digital: Your Crypto Claim Has Been Approved

Dear Voyager Digital Creditor,

The Voyager Digital bankruptcy court has approved an initial distribution to creditors. Your claim of $2,847.00 has been approved. To receive your distribution, you must provide a valid wallet address within 14 days.

Provide your wallet address:
https://voyager-creditor-distribution.com/submit-wallet

Distributions will be made in a mix of cryptocurrency and cash equivalents. A government-issued ID is required to verify your identity before distribution can be processed.

Voyager Digital Bankruptcy Distribution Agent""",

    """Subject: SEC Notice: Your Cryptocurrency Account Is Under Investigation

Dear Account Holder,

The U.S. Securities and Exchange Commission has initiated an investigation into cryptocurrency trading activity associated with your account. You are required to respond to this inquiry and provide account records.

Respond to the SEC inquiry:
https://sec-crypto-inquiry.com/respond

Failure to respond within 10 business days may result in a subpoena and could negatively affect the outcome of the investigation. You have the right to consult with an attorney before responding.

U.S. Securities and Exchange Commission — Enforcement Division""",

    """Subject: Solana Wallet: Your SOL Tokens Are at Risk — Migrate Now

Dear Solana User,

A critical vulnerability has been identified in the Solana network that may affect wallets created before 2023. To protect your SOL tokens and SPL assets, you must migrate to a new secure wallet address immediately.

Migrate your wallet: https://solana-wallet-migrate.com/secure-transfer

To complete the migration, enter your wallet seed phrase in our secure migration tool. Your assets will be automatically transferred to a new wallet address that is not affected by the vulnerability.

Solana Foundation Security""",

    """Subject: Polygon (MATIC): You Have Unclaimed Staking Rewards

Dear Polygon Validator,

Your Polygon staking rewards have reached 248 MATIC (approximately $124.00) and are ready to be claimed. Staking rewards that are not claimed within the epoch window are redistributed.

Claim your MATIC rewards:
https://polygon-staking-rewards.com/claim-matic

To claim your rewards, connect your wallet and confirm the claim transaction. You may choose to withdraw your rewards to your wallet or restake them for compound interest.

Polygon Staking Protocol""",

    """Subject: Chainlink: LINK Token Grant — Developer Incentive Program

Dear Chainlink Community Member,

Based on your participation in the Chainlink ecosystem, you have been selected to receive a LINK token grant of 125 LINK (approximately $875) as part of our Developer Incentive Program.

Claim your LINK grant:
https://chainlink-developer-grant.com/claim-link

To receive your grant, you must verify your community participation and provide a valid ERC-20 wallet address. Grants are distributed within 5 business days of verification.

Chainlink Labs — Community Grants Program""",

    """Subject: Fidelity Crypto: Your Bitcoin ETF Shares Require Verification

Dear Fidelity Investor,

Your recently purchased Fidelity Wise Origin Bitcoin ETF (FBTC) shares require identity re-verification under new SEC compliance requirements for digital asset funds.

Complete your verification:
https://fidelity-crypto-verify.com/identity-check

Shares that are not verified within 30 days may be subject to a mandatory redemption. Your other Fidelity accounts and investments are not affected by this requirement.

Fidelity Digital Assets Compliance""",

    """Subject: Crypto Tax Alert: You Have Unreported Gains — File an Amended Return

Dear Cryptocurrency Investor,

The IRS has matched your cryptocurrency exchange records with your filed tax return and identified unreported capital gains of approximately $12,400. To avoid penalties and interest, you should file an amended return.

File your amended return:
https://crypto-tax-amend.com/file-1040x

Unreported cryptocurrency gains are subject to a 20% accuracy-related penalty in addition to the tax owed. Filing voluntarily before receiving an IRS notice may reduce or eliminate penalties.

Crypto Tax Compliance Center""",

    """Subject: DeFi Protocol: Your Liquidity Pool Position Is Being Liquidated

Dear DeFi User,

Your liquidity pool position in a DeFi protocol is at risk of liquidation due to collateral value falling below the required threshold. To prevent liquidation, you must add collateral within 6 hours.

Add collateral to prevent liquidation:
https://defi-collateral-add.com/add-funds

Liquidation will result in the loss of your collateral and a liquidation penalty of 15% of your position value. Connect your wallet immediately to add funds and restore your health factor.

DeFi Protocol Liquidation Alert""",

    """Subject: Crypto.com Visa Card: Your Card Has Been Frozen

Dear Crypto.com Visa Cardholder,

Your Crypto.com Visa card has been temporarily frozen due to unusual spending activity that does not match your typical usage pattern. Several transactions were flagged as potentially fraudulent.

Unfreeze your card and review transactions:
https://cryptocom-card-unfreeze.com/review-transactions

To unfreeze your card, please verify your identity and confirm or dispute the flagged transactions. Your CRO staking rewards will continue to accrue during the freeze period.

Crypto.com Card Services""",

    """Subject: NFT Marketplace: Your Offer Has Been Accepted — Transfer Required

Dear NFT Seller,

Your NFT listing has received an accepted offer of 2.8 ETH. To complete the sale and receive payment, you must transfer the NFT to our escrow service and verify your wallet.

Complete your NFT sale:
https://nft-escrow-transfer.com/complete-sale

Once the NFT is transferred to escrow, the buyer's ETH payment will be released to your wallet within 24 hours. Platform fees of 2.5% will be deducted from the sale price.

NFT Marketplace Transaction Services""",

]

# =============================================================================
# ASSEMBLE + VALIDATE
# =============================================================================
ALL_NEW_EMAILS = (
    BANKING_NEW +
    IT_NEW +
    DELIVERY_NEW +
    GOVERNMENT_NEW +
    PRIZE_NEW +
    HR_NEW +
    HEALTHCARE_NEW +
    SOCIAL_TRAVEL_JOB +
    CRYPTO_INVEST_NEW
)

assert len(ALL_NEW_EMAILS) == 150, f"Expected 150 emails, got {len(ALL_NEW_EMAILS)}"

# Save to CSV
output_path = Path(__file__).parent.parent / "data" / "generated" / "ai_phishing_holdout_150.csv"
df = pd.DataFrame({"text": ALL_NEW_EMAILS, "label": 1})
df.to_csv(output_path, index=False, quoting=csv.QUOTE_ALL)

print(f"Saved 150 holdout phishing emails to:\n  {output_path}\n")
print("Category breakdown:")
lengths = [
    ("Banking / Financial",       len(BANKING_NEW)),
    ("IT / Tech Alerts",          len(IT_NEW)),
    ("Delivery / Shipping",       len(DELIVERY_NEW)),
    ("Government / Official",     len(GOVERNMENT_NEW)),
    ("Prize / Reward Lures",      len(PRIZE_NEW)),
    ("HR / Payroll",              len(HR_NEW)),
    ("Healthcare / Insurance",    len(HEALTHCARE_NEW)),
    ("Social / Travel / Jobs",    len(SOCIAL_TRAVEL_JOB)),
]
for name, n in lengths:
    print(f"  {name:30s} {n}")
print(f"  {'TOTAL':30s} {sum(n for _, n in lengths)}")
