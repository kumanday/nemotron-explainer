```json
{
  "inventory": [
    {
      "time_s": 0.5,
      "objects": [
        {
          "description": "Full-bleed tide pool footage showing rocks, anemones, seaweed, and water.",
          "box": [0, 0, 1920, 1080]
        }
      ],
      "text": []
    },
    {
      "time_s": 1.5,
      "objects": [
        {
          "description": "Full-bleed tide pool footage showing rocks, anemones, seaweed, and water.",
          "box": [0, 0, 1920, 1080]
        }
      ],
      "text": []
    },
    {
      "time_s": 2.6,
      "objects": [
        {
          "description": "Navy background filling the frame.",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Phone screen displaying tide pool footage, rising from bottom, cut off by bottom frame edge.",
          "box": [211, 613, 492, 1080]
        },
        {
          "description": "Small yellow dot representing tide position.",
          "box": [1140, 486, 1150, 498]
        }
      ],
      "text": []
    },
    {
      "time_s": 3.4,
      "objects": [
        {
          "description": "Navy background filling the frame.",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Phone screen displaying tide pool footage, cut off by bottom frame edge.",
          "box": [211, 414, 492, 1000]
        },
        {
          "description": "Small yellow dot representing tide position.",
          "box": [1249, 463, 1259, 475]
        }
      ],
      "text": []
    },
    {
      "time_s": 4.2,
      "objects": [
        {
          "description": "Navy background filling the frame.",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Phone screen displaying tide pool footage, cut off by bottom frame edge.",
          "box": [211, 414, 492, 1000]
        },
        {
          "description": "Small yellow dot representing tide position.",
          "box": [1520, 523, 1530, 535]
        }
      ],
      "text": []
    },
    {
      "time_s": 5.2,
      "objects": [
        {
          "description": "Navy background filling the frame.",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Phone screen displaying tide pool footage, cut off by bottom frame edge.",
          "box": [211, 414, 492, 1000]
        },
        {
          "description": "Small yellow dot representing tide position near right edge.",
          "box": [1670, 523, 1680, 535]
        }
      ],
      "text": []
    },
    {
      "time_s": 6.4,
      "objects": [
        {
          "description": "Navy background filling the frame.",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Phone screen displaying tide pool footage on the left, cut off by bottom frame edge.",
          "box": [211, 414, 492, 1000]
        },
        {
          "description": "White headline text block on the right.",
          "box": [565, 646, 1690, 980]
        },
        {
          "description": "Teal wordmark text overlapping the headline.",
          "box": [565, 770, 725, 820]
        }
      ],
      "text": [
        "Know the tide before you go.",
        "tidepool",
        "Free on iOS and Android"
      ]
    },
    {
      "time_s": 7.6,
      "objects": [
        {
          "description": "Navy background filling the frame.",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Phone screen displaying tide pool footage on the left, cut off by bottom frame edge.",
          "box": [211, 414, 492, 1000]
        },
        {
          "description": "White headline text block on the right.",
          "box": [565, 646, 1690, 980]
        },
        {
          "description": "Teal wordmark text overlapping the headline.",
          "box": [565, 770, 725, 820]
        }
      ],
      "text": [
        "Know the tide before you go.",
        "tidepool",
        "Free on iOS and Android"
      ]
    }
  ],
  "brief_check": [
    {
      "requirement": "0.0–2.6 s: open full-bleed on the tide-pool clip.",
      "status": "present",
      "evidence": "frame t=0.5: Full-bleed tide pool footage showing rocks, anemones, seaweed, and water. box: [0, 0, 1920, 1080]"
    },
    {
      "requirement": "2.6–5.2 s: footage shrinks into the screen of a phone that rises from the bottom edge.",
      "status": "present",
      "evidence": "frame t=2.6: Phone screen displaying tide pool footage, rising from bottom, cut off by bottom frame edge. box: [211, 613, 492, 1080]"
    },
    {
      "requirement": "Beside the phone, a tide curve draws left to right across six hours.",
      "status": "missing",
      "evidence": "frame t=2.6: Only a small yellow dot is visible, no tide curve line is present."
    },
    {
      "requirement": "a dot rides it to the next low tide, labelled \"Low tide 4:12 PM\".",
      "status": "missing",
      "evidence": "frame t=2.6: A dot is visible but no label \"Low tide 4:12 PM\" exists in any frame."
    },
    {
      "requirement": "5.2–8.0 s: headline \"Know the tide before you go.\" lands beside the phone.",
      "status": "present",
      "evidence": "frame t=6.4: White headline text \"Know the tide before you go.\" visible on the right."
    },
    {
      "requirement": "then the wordmark \"Tidepool\" and the line \"Free on iOS and Android\".",
      "status": "present",
      "evidence": "frame t=6.4: Teal text \"tidepool\" and grey text \"Free on iOS and Android\" visible."
    },
    {
      "requirement": "Phone about 60% of frame height, never cropped.",
      "status": "wrong",
      "evidence": "frame t=2.6: Phone footage is cut off by the bottom frame edge."
    },
    {
      "requirement": "Nothing touches the frame edges except the opening footage.",
      "status": "wrong",
      "evidence": "frame t=2.6: Phone footage touches the bottom frame edge."
    }
  ],
  "scores": {
    "Engagement": 3,
    "Prompt-Intent": 2,
    "Composition": 2,
    "Temporal": 3,
    "Craft": 2
  },
  "findings": [
    {
      "id": "1",
      "axis": "Content",
      "severity": "major",
      "time_s": 2.6,
      "region": {"x": 492, "y": 0, "w": 1920, "h": 1080},
      "saw": "Only a moving dot is visible; the required tide curve line is absent.",
      "suggested_fix": "Animate a tide curve line drawing across the screen beside the phone."
    },
    {
      "id": "2",
      "axis": "Content",
      "severity": "major",
      "time_s": 2.6,
      "region": {"x": 1000, "y": 400, "w": 920, "h": 600},
      "saw": "The label \"Low tide 4:12 PM\" is completely absent from the video.",
      "suggested_fix": "Add the text label \"Low tide 4:12 PM\" near the dot's destination."
    },
    {
      "id": "3",
      "axis": "Craft",
      "severity": "blocker",
      "time_s": 6.4,
      "region": {"x": 565, "y": 770, "w": 725, "h": 100},
      "saw": "The teal wordmark \"tidepool\" overlaps the white headline word \"tide\", making both illegible and messy.",
      "suggested_fix": "Separate the wordmark from the headline or reposition them to avoid overlap."
    },
    {
      "id": "4",
      "axis": "Composition",
      "severity": "major",
      "time_s": 2.6,
      "region": {"x": 211, "y": 613, "w": 281, "h": 467},
      "saw": "The phone screen footage is cut off by the bottom edge of the frame.",
      "suggested_fix": "Scale down the phone or move it up so it is fully contained within the frame."
    }
  ]
}
```