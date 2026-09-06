import os
import urllib.request

OUTPUT_DIR = r"C:\Users\ASUS\Desktop\insurance_denial_audio"

FILES = {
    1: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114638_7fdec209-2990-46a7-9372-8790beb9d09d.mp3",
    2: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_ef7ea422-186f-4a90-90cf-8a25385edea6.mp3",
    3: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_db157ecf-1dcf-44fb-8710-19d8f685e89b.mp3",
    4: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_7f6415ce-7826-4224-8350-8f6b092a7dca.mp3",
    5: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_3dc274cc-c4a2-4143-af26-fe591c1b9164.mp3",
    6: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_44002f91-2fee-4558-93f6-3f21a53771b2.mp3",
    7: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114638_156bfe26-4d98-4b94-8a39-869da69d295c.mp3",
    8: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_f0c719fc-233b-4514-adb7-d12e7bcca9ed.mp3",
    9: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_f051f1bc-1bf0-4e80-8be9-77ccc13562ab.mp3",
    10: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_314a62a3-fac1-4771-9489-17859553c611.mp3",
    11: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_f4f4fbd7-3b3c-4f61-95c3-e98f31367745.mp3",
    12: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114421_4e617db8-53b6-40b0-8641-16e756e14ab0.mp3",
    13: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114639_751b3832-2325-430f-a0f7-343c7d77d81d.mp3",
    14: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_2dd3a7f3-5a26-4a7a-8f92-b18f381f84b1.mp3",
    15: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_2017fc40-b57c-4ff9-ae73-45ff2db9e954.mp3",
    16: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_266567b6-4d6d-4bc0-8b0d-28bc2404a7c0.mp3",
    17: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114531_54dcd252-ab4a-41b5-bfe7-0429bff2b036.mp3",
    18: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_7c268501-7a7f-4b05-b241-01094ce186b6.mp3",
    19: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_f68efbe7-d593-4600-b1a7-d168e2ae2039.mp3",
    20: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_f5e0370a-be54-4443-85e1-48ff9a50cde4.mp3",
    21: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_73e746f8-6225-4155-a362-a4e9fc5570c1.mp3",
    22: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_06e96fa5-ee9d-4cfe-b1c8-af91ca3fbd92.mp3",
    23: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_2ca09488-ad9d-478b-b89a-96ab1ded7a9d.mp3",
    24: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114430_f24b9a9e-0752-428c-8172-10bd841a3da4.mp3",
    25: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114639_fa1d1d4a-b977-4aba-89ce-72c42e080c15.mp3",
    26: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114654_a39f0fb2-422b-46a7-97af-c3c415f013bb.mp3",
    27: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114443_c6765aed-3cdf-4e3a-ba9a-14d13ede66ab.mp3",
    28: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114443_d76b579f-b8bd-43d3-a125-533774bbd47e.mp3",
    29: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114653_5819dacb-99cd-4791-bd1c-7a8726117cb6.mp3",
    30: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114443_8c9c5a52-0e64-4564-8888-27d6c01bcb4a.mp3",
    31: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114653_5acb8f4b-b6b7-4c22-a417-4c7f27bf3120.mp3",
    32: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114443_0b89a66a-6720-4bf2-aba6-2a87e6196f05.mp3",
    33: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114443_19fcff79-f0e8-45e6-8677-c977c619288f.mp3",
    34: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114653_ae441379-4d7d-4b7d-92d3-ffc3060c4d6a.mp3",
    35: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114704_5d71612d-82a1-42ff-a5db-1960e1b517b9.mp3",
    36: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114443_50398414-65fd-4b1b-a1ed-de6996742d66.mp3",
    37: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114456_233e18b2-e67f-46af-91c7-e8bf0bd134ee.mp3",
    38: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114704_d68067fe-0ba5-4d30-a961-e8ee238a31cf.mp3",
    39: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114704_305f322b-c1f0-41ef-8db5-ac00e4f5ca0a.mp3",
    40: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114456_7627bdf2-8b53-4b36-a965-3ced7ccdc9c7.mp3",
    41: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114456_d93c9888-77f7-463d-a2b7-1bc277f57add.mp3",
    42: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114456_bde41762-5a8c-422f-99cb-fa2041cbe2d3.mp3",
    43: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114457_0375d2f1-55bb-4902-a795-f9d966df93ea.mp3",
    44: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114704_a7d5fd36-22ff-4981-b01a-5c8327889572.mp3",
    45: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114456_84cd1ab0-cf29-4d5f-87ac-1189f1df229d.mp3",
    46: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114456_07a6b672-5cd1-43d4-9247-e60a450170c1.mp3",
    47: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114456_90c37494-b902-4564-b785-f3ceacacacce.mp3",
    48: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114714_16cab137-a10c-4129-967d-d45af710d8b9.mp3",
    49: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_73c13a1e-5389-430c-bd1c-c45b3092596f.mp3",
    50: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_22f912a2-2b2f-418e-a006-c746b11d0cc7.mp3",
    51: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_0cfac5af-cef4-43f2-a81f-6a0373cd6c71.mp3",
    52: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_1e6c21e2-be4d-41df-a550-569cec521b46.mp3",
    53: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_9b6cef54-4ff4-4cb3-a085-f6c329852f03.mp3",
    54: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_6536bc8f-e29c-46ce-acfe-799aafac218c.mp3",
    55: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_3287e750-454b-417e-8047-f5abad2558d5.mp3",
    56: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114714_1db64d20-a6ce-4ee2-8d8e-8c8762fe70fe.mp3",
    57: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_3088aff1-1a34-43bc-8f3b-b826e670d051.mp3",
    58: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114714_452aa460-d61a-4e0d-ae9c-f97ad2bb9093.mp3",
    59: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114714_ea01a567-e746-41cd-95f7-c3927677f270.mp3",
    60: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114514_f903707b-46f9-47c0-a116-d36c5002a590.mp3",
    61: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114519_e1d8dde8-5ab8-41c7-a844-065e630c9a65.mp3",
    62: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114519_8f3e367c-6c11-4916-b561-2ecced2a6726.mp3",
    63: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114531_f1bf9250-f0db-4401-b7a7-5188439d863c.mp3",
    64: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114519_d91ce780-c826-4c61-aa52-e57e8e7d1ac0.mp3",
    65: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114531_79aa53eb-cebb-492e-9ddd-2416abd95323.mp3",
    66: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114723_a35a99a4-845c-48d3-9a78-068b9fef0f7a.mp3",
    67: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114519_efeeb4e1-89ac-46ce-8f2f-08e10ac1babd.mp3",
    68: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114519_6dcc9848-dfc6-4d0d-852a-03e3f4b8e63c.mp3",
    69: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114531_73c53418-eeec-49bd-b087-a0b3f6d59b4e.mp3",
    70: "https://d8j0ntlcm91z4.cloudfront.net/user_3IhDaVXfceXJ6vHmiLAhQF3eqEO/hf_20260906_114723_b8cfd22e-d023-40e3-ad7f-f80f2b81f86c.mp3",
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
