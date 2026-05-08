"""Unit tests for crawler helpers — pure functions, no network.

Run with:
    python3 -m unittest tools/xiaoe_quanzi/test_crawler.py
"""
from __future__ import annotations

import unittest

from crawler import classify_form, feed_to_markdown, safe_filename, feed_filename


def _img_post(text: str, n: int = 4) -> dict:
    return {
        "id": "d_test_img",
        "title": "图文测试",
        "nick_name": "一束光线",
        "role_name": "圈主",
        "ip": "1.2.3.4",
        "ip_place": "上海",
        "show_time": "1小时前",
        "created_at": "2026-05-01 10:00:00",
        "feeds_type": 1,
        "zan_num": 3,
        "comment_count": 2,
        "share_num": 1,
        "tags": [{"tag_name": "美股"}, {"tag_name": "国际宏观"}],
        "content": {
            "text": text,
            "mix_records": [
                {"type": "IMAGE", "url": f"https://cdn.example/img{i}.jpg"} for i in range(n)
            ],
        },
    }


def _video_post() -> dict:
    return {
        "id": "d_test_vid",
        "title": "视频测试",
        "nick_name": "一束光线",
        "role_name": "圈主",
        "ip_place": "四川",
        "show_time": "2小时前",
        "created_at": "2026-05-02 11:00:00",
        "feeds_type": 1,
        "zan_num": 0,
        "comment_count": 0,
        "share_num": 0,
        "tags": [],
        "content": {
            "text": "",
            "mix_records": [
                {"type": "VIDEO", "url": "https://v.example/main.m3u8", "showUrl": "https://v.example/poster.jpg"}
            ],
        },
    }


def _file_post() -> dict:
    return {
        "id": "d_test_file",
        "title": "文件测试",
        "nick_name": "一束光线",
        "role_name": "圈主",
        "ip_place": "北京",
        "show_time": "1天前",
        "created_at": "2026-04-30 09:00:00",
        "feeds_type": 1,
        "zan_num": 0,
        "comment_count": 0,
        "share_num": 0,
        "tags": [],
        "content": {"text": "研报附件", "mix_records": []},
        "file_json": [
            {"name": "report.pdf", "url": "https://files.example/r.pdf", "size": 1234, "fileType": "pdf", "down_num": 5}
        ],
    }


def _short_text_post() -> dict:
    return {
        "id": "d_test_short",
        "title": "纯文本短",
        "nick_name": "一束光线",
        "role_name": "圈主",
        "ip_place": "上海",
        "show_time": "10分钟前",
        "created_at": "2026-05-07 09:00:00",
        "feeds_type": 1,
        "zan_num": 0,
        "comment_count": 0,
        "share_num": 0,
        "tags": [],
        "content": {"text": "短消息", "mix_records": []},
    }


class TestClassifier(unittest.TestCase):
    def test_short_text(self):
        self.assertEqual(classify_form(_short_text_post()), "短文（无媒体）")

    def test_long_text(self):
        long = _short_text_post()
        long["content"]["text"] = "x" * 400
        self.assertEqual(classify_form(long), "长文（无媒体）")

    def test_medium_text(self):
        mid = _short_text_post()
        mid["content"]["text"] = "x" * 100
        self.assertEqual(classify_form(mid), "中等文（无媒体）")

    def test_short_with_image(self):
        self.assertEqual(classify_form(_img_post("短", n=1)), "短文+图")

    def test_long_with_image(self):
        self.assertEqual(classify_form(_img_post("x" * 200, n=4)), "长文+图")

    def test_video_post(self):
        self.assertEqual(classify_form(_video_post()), "视频帖")

    def test_file_post(self):
        self.assertEqual(classify_form(_file_post()), "文件帖")

    def test_file_post_takes_priority_over_video(self):
        p = _file_post()
        p["content"]["mix_records"] = [{"type": "VIDEO", "url": "x"}]
        self.assertEqual(classify_form(p), "文件帖")


class TestMarkdown(unittest.TestCase):
    def test_renders_tags_from_tags_array(self):
        md = feed_to_markdown(_img_post("hello", n=1))
        self.assertIn("#美股", md)
        self.assertIn("#国际宏观", md)

    def test_uses_ip_place_for_region(self):
        md = feed_to_markdown(_img_post("hello", n=1))
        self.assertIn("上海", md)
        self.assertNotIn("1.2.3.4", md)

    def test_video_section_includes_poster_and_url(self):
        md = feed_to_markdown(_video_post())
        self.assertIn("封面:", md)
        self.assertIn("main.m3u8", md)

    def test_file_section_lists_attachment(self):
        md = feed_to_markdown(_file_post())
        self.assertIn("report.pdf", md)
        self.assertIn("1234 bytes", md)

    def test_empty_text_falls_back(self):
        post = _video_post()
        md = feed_to_markdown(post)
        self.assertIn("(空)", md)


class TestFilename(unittest.TestCase):
    def test_safe_filename_keeps_chinese(self):
        self.assertEqual(safe_filename("4月ADP数据"), "4月ADP数据")

    def test_safe_filename_strips_unsafe(self):
        self.assertEqual(safe_filename("a / b ? c"), "a_b_c")

    def test_feed_filename_format(self):
        name = feed_filename(_img_post("hi", 1))
        self.assertTrue(name.startswith("2026-05-01_d_test_img"))
        self.assertTrue(name.endswith(".md"))


if __name__ == "__main__":
    unittest.main()
