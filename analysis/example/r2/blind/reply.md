```json
{
  "inventory": [
    {
      "time_s": 0.5,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Full-bleed footage of a tide pool with rocky bottom, sea anemones, seaweed, and rippling water at golden hour."
        }
      ],
      "text": []
    },
    {
      "time_s": 1.5,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Full-bleed footage of a tide pool with rocky bottom, sea anemones, seaweed, and rippling water at golden hour."
        }
      ],
      "text": []
    },
    {
      "time_s": 2.6,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Solid deep ocean navy background."
        },
        {
          "box": [1145, 475, 10, 10],
          "description": "Small warm sand colored dot near center-right."
        }
      ],
      "text": []
    },
    {
      "time_s": 3.4,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Solid deep ocean navy background."
        },
        {
          "box": [1245, 475, 10, 10],
          "description": "Small warm sand colored dot right of center."
        }
      ],
      "text": []
    },
    {
      "time_s": 4.2,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Solid deep ocean navy background."
        },
        {
          "box": [1510, 520, 10, 10],
          "description": "Small warm sand colored dot far right."
        }
      ],
      "text": []
    },
    {
      "time_s": 5.2,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Solid deep ocean navy background."
        }
      ],
      "text": [
        {
          "box": [1135, 460, 730, 490],
          "content": "Low tide 4:12 PM"
        },
        {
          "box": [1115, 500, 940, 690],
          "content": "Know the tide before you go."
        },
        {
          "box": [1115, 690, 250, 740],
          "content": "Tidepool"
        },
        {
          "box": [1115, 795, 765, 830],
          "content": "Free on iOS and Android"
        }
      ]
    },
    {
      "time_s": 6.4,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Solid deep ocean navy background."
        }
      ],
      "text": [
        {
          "box": [1135, 460, 730, 490],
          "content": "Low tide 4:12 PM"
        },
        {
          "box": [1115, 500, 940, 690],
          "content": "Know the tide before you go."
        },
        {
          "box": [1115, 690, 250, 740],
          "content": "Tidepool"
        },
        {
          "box": [1115, 795, 765, 830],
          "content": "Free on iOS and Android"
        }
      ]
    },
    {
      "time_s": 7.6,
      "objects": [
        {
          "box": [0, 0, 1920, 1080],
          "description": "Solid deep ocean navy background."
        }
      ],
      "text": [
        {
          "box": [1135, 460, 730, 490],
          "content": "Low tide 4:12 PM"
        },
        {
          "box": [1115, 500, 940, 690],
          "content": "Know the tide before you go."
        },
        {
          "box": [1115, 690, 250, 740],
          "content": "Tidepool"
        },
        {
          "box": [1115, 795, 765, 830],
          "content": "Free on iOS and Android"
        }
      ]
    }
  ],
  "brief_check": [
    {
      "requirement": "0.0–2.6 s: open full-bleed on the tide-pool clip",
      "status": "present",
      "evidence": "frame t=0.5: full-bleed tide pool footage; frame t=1.5: full-bleed tide pool footage"
    },
    {
      "requirement": "a thin horizon of light sweeps once across the frame",
      "status": "missing",
      "evidence": "frame t=0.5 and t=1.5 show static identical footage with no visible light sweep animation"
    },
    {
      "requirement": "2.6–5.2 s: the footage shrinks into the screen of a phone that rises from the bottom edge",
      "status": "missing",
      "evidence": "frame t=2.6, t=3.4, t=4.2 show only navy background and a dot, no phone or footage"
    },
    {
      "requirement": "Beside the phone, a tide curve draws left to right across six hours and a dot rides it to the next low tide",
      "status": "missing",
      "evidence": "frame t=2.6, t=3.4, t=4.2 show only a dot on navy background, no curve line"
    },
    {
      "requirement": "labelled \"Low tide 4:12 PM\"",
      "status": "present",
      "evidence": "frame t=5.2: text \"Low tide 4:12 PM\" visible"
    },
    {
      "requirement": "5.2–8.0 s: headline \"Know the tide before you go.\" lands beside the phone",
      "status": "wrong",
      "evidence": "frame t=5.2: headline present but no phone beside it"
    },
    {
      "requirement": "wordmark \"Tidepool\"",
      "status": "present",
      "evidence": "frame t=5.2: text \"Tidepool\" visible"
    },
    {
      "requirement": "line \"Free on iOS and Android\"",
      "status": "present",
      "evidence": "frame t=5.2: text \"Free on iOS and Android\" visible"
    },
    {
      "requirement": "Everything settles and holds still for the final second",
      "status": "present",
      "evidence": "frame t=6.4 and t=7.6 show identical static text layout"
    },
    {
      "requirement": "Phone about 60% of frame height, never cropped",
      "status": "missing",
      "evidence": "frame t=5.2, t=6.4, t=7.6 show no phone object"
    },
    {
      "requirement": "Nothing touches the frame edges except the opening footage",
      "status": "present",
      "evidence": "frame t=5.2: text and background elements are inset from edges"
    }
  ],
  "scores": {
    "Engagement": 2,
    "Prompt-Intent": 1,
    "Composition": 2,
    "Temporal": 2,
    "Craft": 3
  },
  "findings": [
    {
      "id": 1,
      "axis": "Prompt-Intent",
      "severity": "blocker",
      "time_s": 2.6,
      "region": {"x": 0, "y": 0, "w": 1920, "h": 1080},
      "saw": "Navy background with a small dot, no phone screen or tide-pool footage visible",
      "suggested_fix": "Animate the tide-pool footage shrinking into a phone that rises from the bottom edge between 2.6s and 5.2s"
    },
    {
      "id": 2,
      "axis": "Prompt-Intent",
      "severity": "major",
      "time_s": 2.6,
      "region": {"x": 0, "y": 0, "w": 1920, "h": 1080},
      "saw": "No tide curve line visible, only a moving dot",
      "suggested_fix": "Draw a tide curve line across the screen with the dot riding it"
    },
    {
      "id": 3,
      "axis": "Composition",
      "severity": "major",
      "time_s": 5.2,
      "region": {"x": 1115, "y": 500, "w": 940, "h": 190},
      "saw": "Headline text appears floating on navy background without the phone beside it",
      "suggested_fix": "Position the phone to the left of the text block as specified in the brief"
    },
    {
      "id": 4,
      "axis": "Temporal",
      "severity": "major",
      "time_s": 2.6,
      "region": {"x": 0, "y": 0, "w": 1920, "h": 1080},
      "saw": "The 2.6s-5.2s segment is empty navy background instead of the phone animation sequence",
      "suggested_fix": "Implement the phone rise and tide curve animation during this interval"
    }
  ]
}
```