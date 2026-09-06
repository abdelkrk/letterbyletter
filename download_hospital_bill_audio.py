import os
import urllib.request

OUTPUT_DIR = r"C:\Users\ASUS\Desktop\hospital_bill_audio"

FILES = {
    1: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124303_7a3f553f-f9ed-4a17-a1c7-b6120a1f3c46.mp3",
    2: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124532_733f300f-c593-41d6-897a-a36778ebf778.mp3",
    3: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124303_e4b542c2-2c57-4938-b7c9-5b90313accdc.mp3",
    4: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124532_cd4303af-9c50-449a-98fb-585e66a27ae6.mp3",
    5: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124533_f9c4dab7-4fc8-4405-8559-f216115e2770.mp3",
    6: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124304_b813b837-c71a-4d38-9ae7-af7795b140ad.mp3",
    7: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124303_e0602500-d5e4-43d1-b563-a443e7a6541e.mp3",
    8: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124532_10783ec0-022b-425a-bafb-e80f3ff37b23.mp3",
    9: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124549_6610b077-c165-4031-844b-2a580d934af3.mp3",
    10: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124549_072b3bba-65a3-4819-b806-25540ebdab4f.mp3",
    11: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124303_56de45f0-08d0-4fe8-b01f-f59ece5bb0c8.mp3",
    12: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124303_da3cacc2-1a15-4325-b772-3f01b5deea5b.mp3",
    13: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_4a260b14-6894-479c-85ee-edb3e4070cf7.mp3",
    14: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_7ae0872c-ba73-4c97-ad4d-5a5d394d9117.mp3",
    15: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_23435522-8f76-448c-846b-6ba7fdc24a40.mp3",
    16: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_c0e4c9e6-0304-452d-90e4-ff2026ea464f.mp3",
    17: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_71800c3a-5b68-4fba-890c-fb62455be7a1.mp3",
    18: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_8b8d6ea9-a640-4e60-84fa-576df51f526c.mp3",
    19: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_3a655e1a-8183-446e-998d-50f4727cb8a9.mp3",
    20: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_a1323dda-c44a-4aa7-922d-d4dc96603c9e.mp3",
    21: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124312_ae9334e6-86e1-469c-b401-8e03f7b35c50.mp3",
    22: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124421_460b01e7-fc50-4e47-b46b-0d9732d6b688.mp3",
    23: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124421_3d50b0f3-e32e-4a97-b6dd-83a871081cd3.mp3",
    24: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124421_9478ceaa-608d-4d03-94ee-dd376e22e60f.mp3",
    25: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124325_94302509-ef0e-484f-94df-3b5d284c22e6.mp3",
    26: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124549_c678ef87-28d4-4b81-b1a4-6da5ceaeb1bf.mp3",
    27: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124325_b2f8963b-7f82-4dcf-aa34-19ccc62c8201.mp3",
    28: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124325_4405b7b1-fdec-4844-b666-590240bcbb14.mp3",
    29: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124549_132577e2-fe06-46e9-9075-0b3dacdd1063.mp3",
    30: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124604_624bb0b3-9bfb-47b1-b808-05dc2ca0b7bf.mp3",
    31: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124325_c6997ec6-f6ff-4d8f-9d9c-32ecfd3c64a0.mp3",
    32: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124325_3222d2b9-c8dd-4e1a-a0ac-3f14df352e4e.mp3",
    33: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124601_ff9a1a17-8dbe-480b-aeba-ee5be4bd72b4.mp3",
    34: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124601_2b07fba8-45b2-464a-8773-3dc281d7e73b.mp3",
    35: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124601_5543330c-5036-4b38-b058-240640d0e765.mp3",
    36: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124325_94ed64be-63c8-4c08-bdab-2e34b8539967.mp3",
    37: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124338_0c21731c-fe9a-435d-9d0c-4694896baa31.mp3",
    38: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124338_7bf1c1b8-3ac3-46de-98a7-256a2dd0e7b8.mp3",
    39: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124338_efac504e-af88-4f25-a62d-72d2ee1ab6be.mp3",
    40: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124338_7a45feab-8617-4804-a43d-4b84902ebe6d.mp3",
    41: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124619_97b1d828-31ca-4073-bc30-766cfc5a3876.mp3",
    42: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124339_10cef072-c6bb-4297-a01a-8e8a00339158.mp3",
    43: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124338_63b719b1-b3a5-4862-8d8e-3ac15213dd97.mp3",
    44: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124338_2f26489d-fe0f-4c45-8e43-82a926f6049a.mp3",
    45: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124620_e833ac5f-6298-4ac4-b555-9f8fd0f79667.mp3",
    46: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124619_4f6692cf-8976-4986-b269-8ee4dde515f7.mp3",
    47: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124339_24891310-bee4-4891-b8f2-5ac7d3748f92.mp3",
    48: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124338_ba43655f-040b-4653-a3f9-02ed087c9e27.mp3",
    49: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124619_45e056b7-ac33-4c33-9db0-9b08573ff66a.mp3",
    50: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124353_a1bc6d00-0dbb-4d12-8b2b-9ffa559209f1.mp3",
    51: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124353_c4ac29e5-169c-42df-899e-bcd85e18581e.mp3",
    52: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124353_dda9825a-f81a-4883-8268-abea6e066b37.mp3",
    53: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124631_a7a75dcf-efb2-4eb7-b3b9-fbcbb33ee314.mp3",
    54: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124353_7aece682-d549-41dd-ab56-78f7c4e551fb.mp3",
    55: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124631_f256cd7f-24c0-4645-bdf1-72a260a6c2d0.mp3",
    56: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124632_17e70651-cc0b-4382-803e-2db571348d1c.mp3",
    57: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124353_e4a8ebda-5bf1-4fb8-813f-67a7670cf8ed.mp3",
    58: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124353_a1fd51c2-2d3e-4fe0-a60e-dd1cd4d8ecb2.mp3",
    59: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124631_14474552-c618-4ac1-8eb7-5448a4734a99.mp3",
    60: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124353_0610ecc1-f9a2-4da4-8a63-935d93fe8809.mp3",
    61: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124409_a0ef8609-c64a-45a9-a282-ec55d2500060.mp3",
    62: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124646_0b0c0501-8ad8-48b2-b016-daed70946be7.mp3",
    63: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124409_bb745966-2016-4ab1-b342-e60e8ec6649a.mp3",
    64: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124646_a1d2c8d0-3962-4444-88c0-9369b1c443e9.mp3",
    65: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124409_499e5864-140a-4b03-8bc6-868ae5936f7c.mp3",
    66: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124646_0742fabd-21b0-4e31-b3a6-ca20d6850aef.mp3",
    67: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124646_487604e4-b06d-4250-96a3-8612d3349007.mp3",
    68: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124409_545ca7fe-6924-4eb5-aeb2-817deaa7f2c1.mp3",
    69: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124657_f5fc956f-eba7-42d3-a17e-9423d47a6e37.mp3",
    70: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124657_6e6d00a2-59b3-43f0-9652-179242e9f1fb.mp3",
    71: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_124409_946bd215-cebd-45cd-9e00-1c6e297cb45b.mp3",
}


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for image_num, url in sorted(FILES.items()):
        dest = os.path.join(OUTPUT_DIR, f"image_{image_num}.mp3")
        print(f"Downloading image_{image_num}.mp3 ...")
        urllib.request.urlretrieve(url, dest)
    print(f"Done. {len(FILES)} files saved to '{OUTPUT_DIR}/'.")


if __name__ == "__main__":
    main()
