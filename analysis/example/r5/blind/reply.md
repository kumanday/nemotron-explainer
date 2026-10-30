```json
{
  "inventory": [
    {
      "time_s": 0.5,
      "objects": [
        {
          "description": "Full-frame tide pool footage with anemones, rocks, seaweed, and rippling water",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Horizontal bright light reflection or streak across center of frame",
          "box": [0, 430, 1920, 520]
        }
      ],
      "text": []
    },
    {
      "time_s": 1.5,
      "objects": [
        {
          "description": "Full-frame tide pool footage with anemones, rocks, seaweed, and rippling water",
          "box": [0, 0, 1920, 1080]
        }
      ],
      "text": []
    },
    {
      "time_s": 2.6,
      "objects": [
        {
          "description": "Tide pool footage inside a rounded rectangle on left side of screen",
          "box": [390, 310, 940, 910]
        },
        {
          "description": "Solid navy background filling remainder of frame",
          "box": [0, 0, 1920, 1080]
        },
        {
          "description": "Small pale dot on right side of frame",
          "box": [1145, 485, 1160, 500]
        }
      ],
      "text": []
    },
    {
      "time_s": 3.4,
      "objects": [
        {
          "description": "Tide pool footage inside a rounded rectangle on left side of screen",
          "box": [390, 310, 940, 910]
        },
        {
          "description": "Short teal curved line on right side",
          "box": [1145, 480, 1285, 495]
        },
        {
          "description": "Small dot at right end of teal curve",
          "box": [1280, 480, 1295, 495]
        }
      ],
      "text": []
    },
    {
      "time_s": 4.2,
      "objects": [
        {
          "description": "Tide pool footage inside a rounded rectangle on left side of screen",
          "box": [390, 310, 940, 910]
        },
        {
          "description": "Longer teal curved line extending across right side",
          "box": [1145, 505, 1620, 545]
        },
        {
          "description": "Small dot at right end of teal curve",
          "box": [1615, 540, 1630, 550]
        }
      ],
      "text": []
    },
    {
      "time_s": 5.2,
      "objects": [
        {
          "description": "Tide pool footage inside a rounded rectangle on left side of screen",
          "box": [390, 310, 940, 910]
        },
        {
          "description": "Text label 'Low tide 4:12 PM' in warm sand color",
          "box": [1125, 440, 1350, 470]
        },
        {
          "description": "Headline text 'Know the tide before you go.' in white",
          "box": [1100, 530, 1900, 720]
        },
        {
          "description": "Wordmark 'Tidepool' in teal",
          "box": [1100, 760, 1350, 810]
        },
        {
          "description": "Body text 'Free on iOS and Android' in gray",
          "box": [1100, 880, 1700, 910]
        }
      ],
      "text": [
        "Low tide 4:12 PM",
        "Know the tide before you go.",
        "Tidepool",
        "Free on iOS and Android"
      ]
    },
    {
      "time_s": 6.4,
      "objects": [
        {
          "description": "Tide pool footage inside a rounded rectangle on left side of screen",
          "box": [390, 310, 940, 910]
        },
        {
          "description": "Text label 'Low tide 4:12 PM' in warm sand color",
          "box": [1125, 440, 1350, 470]
        },
        {
          "description": "Headline text 'Know the tide before you go.' in white",
          "box": [1100, 530, 1900, 720]
        },
        {
          "description": "Wordmark 'Tidepool' in teal",
          "box": [1100, 760, 1350, 810]
        },
        {
          "description": "Body text 'Free on iOS and Android' in gray",
          "box": [1100, 880, 1700, 910]
        }
      ],
      "text": [
        "Low tide 4:12 PM",
        "Know the tide before you go.",
        "Tidepool",
        "Free on iOS and Android"
      ]
    },
    {
      "time_s": 7.6,
      "objects": [
        {
          "description": "Tide pool footage inside a rounded rectangle on left side of screen",
          "box": [390, 310, 940, 910]
        },
        {
          "description": "Text label 'Low tide 4:12 PM' in warm sand color",
          "box": [1125, 440, 1350, 470]
        },
        {
          "description": "Headline text 'Know the tide before you go.' in white",
          "box": [1100, 530, 1900, 720]
        },
        {
          "description": "Wordmark 'Tidepool' in teal",
          "box": [1100, 760, 1350, 810]
        },
        {
          "description": "Body text 'Free on iOS and Android' in gray",
          "box": [1100, 880, 1700, 910]
        }
      ],
      "text": [
        "Low tide 4:12 PM",
        "Know the tide before you go.",
        "Tidepool",
        "Free on iOS and Android"
      ]
    }
  ],
  "brief_check": [
    {
      "requirement": "0.0–2.6 s: open full-bleed on the tide-pool clip",
      "status": "present",
      "evidence": "frame t=0.5: full-frame tide pool footage filling 1920x1080"
    },
    {
      "requirement": "0.0–2.6 s: a thin horizon of light sweeps once across the frame",
      "status": "present",
      "evidence": "frame t=0.5: horizontal bright light reflection across center of frame"
    },
    {
      "requirement": "2.6–5.2 s: the footage shrinks into the screen of a phone that rises from the bottom edge, still playing",
      "status": "missing",
      "evidence": "frame t=2.6: footage is in a rounded rectangle on the left, not a phone, and not rising from the bottom edge"
    },
    {
      "requirement": "Beside the phone, a tide curve draws left to right across six hours",
      "status": "missing",
      "evidence": "frame t=4.2: teal curve is present but no phone exists beside it, and no hour markers indicate six hours"
    },
    {
      "requirement": "a dot rides it to the next low tide, labelled 'Low tide 4:12 PM'",
      "status": "wrong",
      "evidence": "frame t=5.2: label 'Low tide 4:12 PM' appears at 5.2s instead of accompanying the dot during the 2.6–5.2s interval"
    },
    {
      "requirement": "5.2–8.0 s: headline 'Know the tide before you go.' lands beside the phone",
      "status": "wrong",
      "evidence": "frame t=5.2: headline is present but beside a rounded video rectangle, not a phone"
    },
    {
      "requirement": "then the wordmark 'Tidepool' and the line 'Free on iOS and Android'",
      "status": "present",
      "evidence": "frame t=5.2: both 'Tidepool' and 'Free on iOS and Android' are visible"
    },
    {
      "requirement": "Everything settles and holds still for the final second",
      "status": "present",
      "evidence": "frame t=6.4 and t=7.6: composition is identical and static"
    },
    {
      "requirement": "Phone about 60% of frame height, never cropped",
      "status": "missing",
      "evidence": "frame t=5.2: no phone is visible, only a rounded video rectangle approximately 55% of frame height"
    },
    {
      "requirement": "Nothing touches the frame edges except the opening footage",
      "status": "present",
      "evidence": "frame t=2.6: rounded rectangle and all elements are inset from frame edges"
    }
  ],
  "scores": {
    "Engagement": 3,
    "Prompt-Intent": 2,
    "Composition": 3,
    "Temporal": 3,
    "Craft": 3
  },
  "findings": [
    {
      "id": "F1",
      "axis": "content",
      "severity": "blocker",
      "time_s": 2.6,
      "region": {"x": 0, "y": 0, "w": 1920, "h": 1080},
      "saw": "footage displayed in a rounded rectangle on the left, no phone device visible",
      "suggested_fix": "animate a phone rising from the bottom edge with the tide pool footage playing on its screen"
    },
    {
      "id": "F2",
      "axis": "timing",
      "severity": "major",
      "time_s": 5.2,
      "region": {"x": 1125, "y": 440, "w": 225, "h": 30},
      "saw": "'Low tide 4:12 PM' label appears at 5.2s after the curve animation ends",
      "suggested_fix": "display the 'Low tide 4:12 PM' label alongside the dot during the 2.6–5.2s interval as the curve draws"
    },
    {
      "id": "F3",
      "axis": "content",
      "severity": "major",
      "time_s": 4.2,
      "region": {"x": 1145, "y": 505, "w": 475, "h": 40},
      "saw": "teal curve has no hour markers and does not visually represent six hours",
      "suggested_fix": "add hour tick marks along the curve and ensure it spans a six-hour duration visually"
    },
    {
      "id": "F4",
      "axis": "craft",
      "severity": "minor",
      "time_s": 5.2,
      "region": {"x": 1100, "y": 880, "w": 600, "h": 30},
      "saw": "'Free on iOS and Android' appears smaller than 32px",
      "suggested_fix": "increase body and label text size to at least 32px as specified"
    }
  ]
}
```